# ckanext-scheme-sddi
The ckanext-theme-sddi is a CKAN extension crafted to provide a specialized theme for the Smart District Data Infrastructure [(SDDI)](https://www.asg.ed.tum.de/en/gis/projects/smart-district-data-infrastructure/).  This extension enhances the CKAN platform by integrating a custom theme that aligns with the SDDI’s visual and functional requirements.

### Funcionality
The SDDI metadata schemas are defined as YAML files under `ckanext/scheme_sddi/`. Each schema corresponds to one of the nine SDDI catalog categories (Datensatz, Software, Methode, Online-Anwendung, Geoobjekt, Online-Dienst, Projekt, Gerät, Digitaler Zwilling).

It is defined according to the following UML diagram:
![UMD-SDDI](https://collab.dvb.bayern/download/attachments/67111968/UML%20Diagram%20SDDI%20%28DT%29%20V4.jpg?version=1&modificationDate=1657288940287&api=v2)

This plugin enables restricted functions for resources.
It is possible to specify that the resources have the following rights:
- public - The resource is be publicly available.
- registered - The resource is available only to users who have an account in the catalog.
- same_organization - Users within the organization for which the catalog entry was created can access the resource.
- only_allowed_users - Only selected users can access the resource.

### Compatibility

Compatibility with core CKAN versions:

| CKAN version    | Compatible?   |
| --------------- | ------------- |
| 2.10            | yes    |
| 2.11            | not yet    |

## Installation

**TODO:** Add any additional install steps to the list below.
   For example installing any non-Python dependencies or adding any required
   config settings.

To install ckanext-scheme-sddi:

1. Activate your CKAN virtual environment, for example:

     . /usr/lib/ckan/default/bin/activate

2. Clone the source and install it on the virtualenv

    git clone https://github.com/Chair of Geoinformatics, Technical University of Munich/ckanext-scheme-sddi.git
    cd ckanext-scheme-sddi
    pip install -e .
	pip install -r requirements.txt

3. Add `scheme_sddi` to the `ckan.plugins` setting in your CKAN
   config file (by default the config file is located at
   `/etc/ckan/default/ckan.ini`).

   ```ini
   ckan.plugins = ... scheming_datasets scheme_sddi
   ```

4. Add the following scheming configuration to your `ckan.ini`:

   ```ini
   ####### scheming config #######
   scheming.dataset_schemas = ckanext.scheme_sddi:sddi_dataset_documents.yaml
                              ckanext.scheme_sddi:sddi_software.yaml
                              ckanext.scheme_sddi:sddi_method.yaml
                              ckanext.scheme_sddi:sddi_online_application.yaml
                              ckanext.scheme_sddi:sddi_geoobject.yaml
                              ckanext.scheme_sddi:sddi_online_service.yaml
                              ckanext.scheme_sddi:sddi_projekt.yaml
                              ckanext.scheme_sddi:sddi_device.yaml
                              ckanext.scheme_sddi:sddi_digital_twin.yaml
   scheming.presets = ckanext.scheming:presets.json ckanext.scheme_sddi:sddi_presets.json
   scheming.dataset_fallback = false
   ```

   Each entry maps to one of the SDDI catalog categories:

   | Schema file | `dataset_type` | Category (UI) |
   |---|---|---|
   | `sddi_dataset_documents.yaml` | `dataset_documents` | Datensatz und Dokumente |
   | `sddi_software.yaml` | `software` | Software |
   | `sddi_method.yaml` | `method` | Methode |
   | `sddi_online_application.yaml` | `online-application` | Online-Anwendung |
   | `sddi_geoobject.yaml` | `geoobject` | Geoobjekt |
   | `sddi_online_service.yaml` | `online-service` | Online-Dienst |
   | `sddi_projekt.yaml` | `project` | Projekt |
   | `sddi_device.yaml` | `device` | Gerät / Ding |
   | `sddi_digital_twin.yaml` | `digital-twin` | Digitaler Zwilling |

   > **Important:** The `dataset_type` value in each YAML file must exactly match
   > the URL path used in the category selection page (`new_type_select.html`).
   > Types with multiple words must use hyphens (e.g. `online-service`), not
   > underscores, to avoid a known CKAN URL-building issue where the first
   > underscore is replaced with a dot when constructing Flask endpoints.

5. Restart CKAN. For example if you've deployed CKAN with Apache on Ubuntu:

     sudo service apache2 reload

## Developer installation

To install ckanext-scheme-sddi for development, activate your CKAN virtualenv and
do:

    git clone https://github.com/Chair of Geoinformatics, Technical University of Munich/ckanext-scheme-sddi.git
    cd ckanext-scheme-sddi
    python setup.py develop
    pip install -r dev-requirements.txt


## Tests

To run the tests, do:

    pytest --ckan-ini=test.ini

## License

[AGPL](https://www.gnu.org/licenses/agpl-3.0.en.html)
