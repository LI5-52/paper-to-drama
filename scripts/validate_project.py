#!/usr/bin/env python3
"""Paper-to-Drama V0.1: deterministic structure / cross-stage reference validation.
No claims of narrative or research truth verification. Standard library only.
"""
import json
import sys
from pathlib import Path


def run(path: Path):
    data = json.loads(path.read_text(encoding='utf-8'))
    errors = []
    required = ['project_id', 'paper', 'research_cards', 'seed', 'core_question',
                'style_options', 'selection', 'story_bible', 'screenplay',
                'assets', 'shots', 'model_prompts', 'qa_log', 'production']
    for key in required:
        if key not in data:
            errors.append(f'missing: {key}')
    if errors:
        return errors

    cards = data['research_cards']
    styles = data['style_options']
    scenes = data['screenplay']['scenes']
    shots = data['shots']
    assets = data['assets']
    prompts = data['model_prompts']
    def idset(items, field='id'):
        ids = [x.get(field) for x in items]
        if None in ids or len(set(ids)) != len(ids):
            errors.append(f'IDs invalid or duplicated: {field}')
        return set(ids)
    cardids = idset(cards)
    styleids = idset(styles)
    sceneids = idset(scenes)
    shotids = idset(shots)
    roleids = idset(assets.get('characters', []))
    locationids = idset(assets.get('locations', []))
    evidences = set(data.get('paper', {}).get('evidence_ids', []))
    for card in cards:
        if not card.get('source_locator'):
            errors.append(f'no source locator: {card.get("id")}')
        if card.get('claim_type') == 'supported_claim' and card.get('evidence_id') not in evidences:
            errors.append(f'unsupported research claim evidence ID: {card.get("id")}')
    seed = data['seed']
    if not seed.get('character_goal') or not seed.get('obstacle') or not seed.get('choice'):
        errors.append('drama seed lacks action goal, obstacle, or choice')
    if not set(seed.get('research_card_ids', [])).issubset(cardids):
        errors.append('drama seed references unknown research card')
    cqid = data['core_question'].get('id')
    if not cqid or seed.get('core_question_id') != cqid:
        errors.append('core question ID mismatch in seed')
    if len(styles) != 3:
        errors.append(f'must give exactly three style options, got {len(styles)}')
    for opt in styles:
        if opt.get('core_question_id') != cqid:
            errors.append(f'style not tied to frozen core question: {opt.get("id")}')
        for key in ['world', 'genre', 'dramatic_engine', 'visual_mode', 'hook', 'premise', 'why_fit']:
            if not opt.get(key):
                errors.append(f'style missing {key}: {opt.get("id")}')
    engines = [x.get('dramatic_engine') for x in styles]
    if len(set(engines)) < 2:
        errors.append('style proposals have no meaningful narrative-mechanism variation')
    chosen = data['selection'].get('selected_style_id')
    if chosen not in styleids:
        errors.append('selected style not found')
    if data['story_bible'].get('selected_style_id') != chosen:
        errors.append('story bible uses different style from user selection')
    for scene in scenes:
        if scene.get('location_id') not in locationids:
            errors.append(f'scene unknown location: {scene.get("id")}')
        if not set(scene.get('character_ids', [])).issubset(roleids):
            errors.append(f'scene unknown character: {scene.get("id")}')
        if not scene.get('what_changes'):
            errors.append(f'scene no meaningful change justification: {scene.get("id")}')
    for sh in shots:
        if sh.get('scene_id') not in sceneids:
            errors.append(f'shot unknown scene: {sh.get("id")}')
        if not set(sh.get('character_ids', [])).issubset(roleids):
            errors.append(f'shot unknown character: {sh.get("id")}')
        if sh.get('location_id') not in locationids:
            errors.append(f'shot unknown location: {sh.get("id")}')
        if not isinstance(sh.get('duration_s'), (int, float)) or sh['duration_s'] <= 0:
            errors.append(f'shot invalid duration: {sh.get("id")}')
        for key in ['purpose', 'start_state', 'visible_action', 'end_state']:
            if not sh.get(key):
                errors.append(f'shot missing {key}: {sh.get("id")}')
    for p in prompts:
        if p.get('shot_id') not in shotids:
            errors.append('video prompt references unknown shot')
    for x in data.get('qa_log', []):
        if not x.get('stage') or not x.get('issue_type') or not x.get('target_id'):
            errors.append('QA log missing stage/type/target')
    if data['production'].get('status') == 'video_ready' and not data['production'].get('verified_result_uri'):
        errors.append('video_ready without independently verified result URI')
    return errors

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: python scripts/validate_project.py <project.json>')
        sys.exit(2)
    path = Path(sys.argv[1])
    errors = run(path)
    if errors:
        print(f'FAILED: {len(errors)} structural issues')
        for e in errors:
            print(' -', e)
        sys.exit(1)
    print('PASS: required structure and cross-stage references are consistent.')
    print('NOTE: semantic accuracy, dramatic quality, viewer appeal, and video output NOT validated.')
