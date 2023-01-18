from constants import SolidatusConstants

def generate_base_entity(name, properties_dict, unique_identifier_property=SolidatusConstants.DEFAULT_UNIQUE_IDENTIFIER_PROPERTY_NAME):
    if unique_identifier_property not in properties_dict:
        raise Exception("Unique identifier must be specified for every entity as that is used when applying updates")
    return {
        "name": name,
        "properties": properties_dict
    }

def generate_transition_entity(source_entity, target_entity, properties_dict, unique_identifier_property=SolidatusConstants.DEFAULT_UNIQUE_IDENTIFIER_PROPERTY_NAME):
    if unique_identifier_property not in properties_dict:
        raise Exception("Unique identifier must be specified for every transition entity as that is used when applying updates")
    return {
        "source": source_entity,
        "target": target_entity,
        "properties": properties_dict
    }

