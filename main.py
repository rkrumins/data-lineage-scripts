import utils
import apply_incremental_updates

def main():
    existing_model_definition = utils.load_model_from_local_filesystem("test_data/sample_base_model.json")
    new_model_model_update_entities = utils.load_model_from_local_filesystem("test_data/new_entities.json")
    updated_model_dict = apply_incremental_updates.apply(existing_model_definition, new_model_model_update_entities)
    json_model_payload = utils.output_dictionary_as_json(updated_model_dict)
    print(json_model_payload)

main()