from constants import SolidatusConstants, SolidatusModelKeyConstants

def generate_base_entity(name, properties_dict, unique_identifier_property=SolidatusConstants.DEFAULT_UNIQUE_IDENTIFIER_PROPERTY_NAME):
    if unique_identifier_property not in properties_dict:
        raise Exception("Unique identifier must be specified for every entity as that is used when applying updates")
    return {
        SolidatusModelKeyConstants.ENTITY_NAME_KEY_NAME: name,
        SolidatusModelKeyConstants.ENTITY_PROPERTIES_KEY_NAME: properties_dict
    }

def generate_transition_entity(source_entity, target_entity, properties_dict, unique_identifier_property=SolidatusConstants.DEFAULT_UNIQUE_IDENTIFIER_PROPERTY_NAME):
    if unique_identifier_property not in properties_dict:
        raise Exception("Unique identifier must be specified for every transition entity as that is used when applying updates")
    return {
        SolidatusModelKeyConstants.TRANSITIONS_SOURCE_ENTITY_KEY_NAME: source_entity,
        SolidatusModelKeyConstants.TRANSITIONS_TARGET_ENTITY_KEY_NAME: target_entity,
        SolidatusModelKeyConstants.TRANSITIONS_PROPERTIES_KEY_NAME: properties_dict
    }

