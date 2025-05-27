import os
import yaml
from pathlib import Path

def update_environment_file(env_path, new_tag):
    with open(env_path, "r") as f:
        data = yaml.safe_load(f)

    if 'parameters' in data:
        data['parameters']['ReleaseTag'] = new_tag

    with open(env_path, "w") as f:
        yaml.dump(data, f)

if __name__ == "__main__":
    ENV_NAME = os.getenv("ENV_NAME", "DEV")
    RELEASE_TAG = os.getenv("RELEASE_TAG", "v1.0.0")

    aem_publish_env = Path("aem_publish/release/environment-definition.yml")
    aem_adaptor_env = Path("aem_adaptor/release/environment-definition.yml")

    update_environment_file(aem_publish_env, RELEASE_TAG)
    update_environment_file(aem_adaptor_env, RELEASE_TAG)
    print("YAML files updated.")
