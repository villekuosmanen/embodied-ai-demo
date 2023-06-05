# embodied-ai-demo

Test playground for Habitat, Embodied AI test environment.

https://aihabitat.org/docs/habitat2/

## Build habitat sim

For M1 MacOS, without conda.

- Ensure you have the Habitat sim git repository cloned at parent level
  - `git clone --branch stable https://github.com/facebookresearch/habitat-sim.git`
- cd `habitat-sim`
- Set env variables
  - export `WITH_BULLET=1`
  - export `HEADLESS=0`
- `pip install . -v`


Download data when running for the first time:
- `python -m habitat_sim.utils.datasets_download --uids habitat_test_scenes --data-path data`
- `python -m habitat_sim.utils.datasets_download --uids habitat_example_objects --data-path data`

## Interactive testing using the `viewer` application

Note: `viewer` is built as part of the above process. You need to disable headless mode (done by setting HEADLESS env var to 0) for the application to be built.

- `../habitat-sim/build/utils/viewer/viewer ../habitat-sim/data/scene_datasets/habitat-test-scenes/skokloster-castle.glb`

## Install habitat lab
- Ensure you have the Habitat lab git repository cloned at parent level
    - `git clone --branch stable https://github.com/facebookresearch/habitat-lab.git`
- `cd habitat-lab`
- `pip install -e habitat-lab`

## Benchmarking

`pytest -v -s test_baseline_agents.py::test_custom_agents`
