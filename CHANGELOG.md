# Changelog

All notable changes to this project will be documented in this file.

## [0.1.0] - Unreleased

### Added
- Extended metadata schema for each SDDI main category: Digital Twin, GeoObject, Method, Software, Online Service, Online Application, Dataset Documents, Device, Project
- German translations for all schema types
- `is_raw_data` and `data_modification` fields with conditional UI visibility to Device schema
- `issued` and `modified` date fields to resource fields across all schemas
- Multi-select field for involved organizations in Project schema
- Extended RoleCode choices in Project schema
- `docs/` folder for schema documentation
- UML-aligned `has_*` yes/no select fields for Distribution-typed attributes in each schema:
  - `dataset_documents`: `has_distribution` → Content URL
  - `project`: `has_distribution` → Project URI
  - `online-service`: `has_linkage`, `has_external_docs`, `has_open_api_document`
  - `software`: `has_software_help`, `has_documentation_url`, `has_code_repository_url`
  - `online-application`: `has_external_docs`, `has_service_doc`
- `docs/` folder updated with current UML diagram (PDF, image, XLSX)

### Changed
- Resource access control field renamed from `distribution_access_rights` to `restricted_level` across all schemas to align with the restricted plugin

### Fixed
- Resource access restrictions were not enforced due to incorrect field name (`distribution_access_rights` instead of `restricted_level`)

### Removed
- `distribution_url` free-text URL field replaced by the above typed yes/no fields
- Distribution section removed from `digital-twin`, `geoobject`, `device`, and `method` — these classes have no Distribution-typed attributes in the UML

### Known issues
- Existing resources with `distribution_access_rights` set must be re-saved to apply access control under the new field name

## [0.0.2] - 2024-02-18
### Added
Add spatial display snippet (see [#6](https://github.com/MarijaKnezevic/ckanext-scheme-sddi/pull/6))

## [0.0.1] - 2024-10-04
- Initial release
- Compatibility with CKAN 2.11.

## [template] - YYYY-MM-DD

### Added

### Changed

### Removed

### Fixed

### Security

### Deprecated

### Known issues

[Unreleased]: https://github.com/MarijaKnezevic/ckanext-scheme-sddi/compare/0.1.0...HEAD
[0.1.0]: https://github.com/MarijaKnezevic/ckanext-scheme-sddi/compare/0.0.2...0.1.0
[0.0.2]: https://github.com/MarijaKnezevic/ckanext-scheme-sddi/compare/0.0.1...0.0.2
[0.0.1]: https://github.com/MarijaKnezevic/ckanext-scheme-sddi/releases/tag/0.0.1
[template]: https://keepachangelog.com/en/1.0.0/
