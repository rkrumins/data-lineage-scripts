import model
import utils
from constants import SolidatusConstants, SolidatusModelKeyConstants


def apply_changes_to_existing_entity_properties():
    pass


def verify_entity_exists_in_model_already():
    pass


def apply(existing_model_dict, new_entities_dict, unique_property_identifier=SolidatusConstants.DEFAULT_UNIQUE_IDENTIFIER_PROPERTY_NAME) -> dict:
    existing_model_unique_property_dict_to_uuid_dict = utils.get_existing_entities_identifier_to_uuid_dict(existing_model_dict, unique_property_identifier)
    print(existing_model_unique_property_dict_to_uuid_dict)
    updated_model = existing_model_dict
    print(updated_model)

    for new_entity_definition in new_entities_dict:
        new_entity_unique_property_identifier = new_entity_definition[unique_property_identifier]

        if new_entity_unique_property_identifier in existing_model_unique_property_dict_to_uuid_dict:
            # Update Existing Entity Definition
            existing_entity_uuid = existing_model_unique_property_dict_to_uuid_dict[new_entity_unique_property_identifier]
            updated_model[SolidatusModelKeyConstants.ENTITIES_KEY_NAME][existing_entity_uuid][SolidatusModelKeyConstants.ENTITY_PROPERTIES_KEY_NAME].update(new_entity_definition)
        else:
            # Add New Entity Definition To The Model
            updated_model[SolidatusModelKeyConstants.ENTITIES_KEY_NAME][new_entity_unique_property_identifier] = model.generate_base_entity("DataElement", new_entity_definition, unique_property_identifier)

    return updated_model
    