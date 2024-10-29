# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------
# pylint: disable=too-many-lines
# pylint: disable=unused-argument
# pylint: disable=too-many-statements

from .aaz.latest.arcgateway.settings import Update as _SettingsUpdate


# hide settings_resource_name from user and always set it to be 'Default'
class SettingsUpdate(_SettingsUpdate):
    """Update the base Settings of the target resource.

    :example: Sample command for setting update
        az arcgateway settings update --resource-group myResourceGroup --subscription mySubscription
        --base-provider Microsoft.HybridCompute --base-resource-type machines
        --base-resource-name workloadServer --gateway-resource-id myResourceId
    """
    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        args_schema = super()._build_arguments_schema(*args, **kwargs)

        # pylint: disable=protected-access
        args_schema.settings_resource_name._required = False
        args_schema.settings_resource_name._registered = False

        return args_schema

    def pre_operations(self):
        args = self.ctx.args
        args.settings_resource_name = "Default"