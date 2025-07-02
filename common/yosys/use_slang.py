def process_input(state_in, config, step_cls, pdk_root, test):
    config_parsed = step_cls._load_config_from_file(config, pdk_root)
    if "slang" in test:
        config_parsed = config_parsed.copy(USE_SLANG=True)

    return state_in, config_parsed
