import json
from constants import SolidatusConstants, SolidatusModelKeyConstants


def load_model_from_local_filesystem(model_path):
    with open(model_path) as f:
        return json.load(f)


def get_existing_entities_identifier_to_uuid_dict(existing_model, unique_identifier_property=SolidatusConstants.DEFAULT_UNIQUE_IDENTIFIER_PROPERTY_NAME):
    model_entities = existing_model[SolidatusModelKeyConstants.ENTITIES_KEY_NAME]
    uuid_to_unique_property_dict = dict()

    for model_entity_uuid, model_entity_definition in model_entities.items():
        unique_property_value_name = model_entity_definition[SolidatusModelKeyConstants.ENTITY_PROPERTIES_KEY_NAME][unique_identifier_property]
        if model_entity_uuid not in uuid_to_unique_property_dict:
            uuid_to_unique_property_dict[unique_property_value_name] = model_entity_uuid
        else:
            raise Exception("UUID key already present in the dictionary")
    
    return uuid_to_unique_property_dict


def get_existing_entity_uuid_to_unique_property_identifier_dict(existing_model, unique_identifier_property=SolidatusConstants.DEFAULT_UNIQUE_IDENTIFIER_PROPERTY_NAME):
    model_entities = existing_model[SolidatusModelKeyConstants.ENTITIES_KEY_NAME]
    uuid_to_unique_property_dict = dict()

    for model_entity_uuid, model_entity_definition in model_entities.items():
        unique_property_value_name = model_entity_definition[SolidatusModelKeyConstants.ENTITY_PROPERTIES_KEY_NAME][unique_identifier_property]
        if model_entity_uuid not in uuid_to_unique_property_dict:
            uuid_to_unique_property_dict[model_entity_uuid] = unique_property_value_name
        else:
            raise Exception("UUID key already present in the dictionary")
    
    return uuid_to_unique_property_dict
