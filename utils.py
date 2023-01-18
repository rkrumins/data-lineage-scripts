import json

def load_model_from_local_filesystem(model_path):
    with open(model_path) as f:
        return json.load(f)

def get_existing_entities_identifier_to_uuid_map(existing_model, unique_identifier_property="path_id"):
    model_entities = existing_model["entities"]
    uuid_to_unique_property_dict = dict()

    for model_entity_uuid, model_entity_definition in model_entities:
        unique_property_value_name = model_entity_definition["properties"][unique_identifier_property]