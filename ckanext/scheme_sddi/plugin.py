import ckan.plugins as plugins
import ckan.plugins.toolkit as tk

import ckanext.scheme_sddi.helpers as helpers
import ckanext.scheme_sddi.validators as validators


class SchemeSddiPlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.IValidators)
    plugins.implements(plugins.ITemplateHelpers)

    # IConfigurer

    def update_config(self, config_):
        tk.add_template_directory(config_, "templates")
        tk.add_public_directory(config_, "public")
        tk.add_resource("assets", "scheme_sddi")

    # ITemplateHelpers

    def get_helpers(self):
        return {
            "composite_get_as_dict": helpers.composite_get_as_dict,
            "composite_get_value_dict": helpers.composite_get_value_dict,
            "composite_get_label_dict": helpers.composite_get_label_dict,
            "composite_get_choices_dict": helpers.composite_get_choices_dict,
            "composite_get_name_list": helpers.composite_get_name_list,
            "composite_repeating_get_value_dict_list": helpers.composite_repeating_get_value_dict_list,
            "composite_is_mail": helpers.composite_is_mail,
            "composite_is_list": helpers.composite_is_list,
            "composite_join_list": helpers.composite_join_list,
            "composite_get_markup": helpers.composite_get_markup,
            "composite_get_default_value": helpers.composite_get_default_value,
        }

    # IValidators

    def get_validators(self):
        return {
            "composite_group2json": validators.composite_group2json,
            "composite_repeating_group2json": validators.composite_repeating_group2json,
        }
