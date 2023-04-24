#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright: (c) 2022, Ansible Project
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# template: header.j2
# This module is autogenerated using the gouttelette generator tool
# See: https://github.com/ansible-collections/gouttelette


DOCUMENTATION = r"""
module: ssm_resource_data_sync
short_description: Creates and manages a resource data sync
description:
- Creates and manages a resource data sync for AWS Systems Manager.
- A resource data sync helps you view data from multiple sources in a single location.
options:
    bucket_name:
        description:
        - Not Provived.
        type: str
    bucket_prefix:
        description:
        - Not Provived.
        type: str
    bucket_region:
        description:
        - Not Provived.
        type: str
    force:
        default: false
        description:
        - Cancel IN_PROGRESS and PENDING resource requestes.
        - Because you can only perform a single operation on a given resource at a
            time, there might be cases where you need to cancel the current resource
            operation to make the resource available so that another operation may
            be performed on it.
        type: bool
    kms_key_arn:
        description:
        - Not Provived.
        type: str
    s3_destination:
        description:
        - Not Provived.
        suboptions:
            bucket_name:
                description:
                - Not Provived.
                type: str
            bucket_prefix:
                description:
                - Not Provived.
                type: str
            bucket_region:
                description:
                - Not Provived.
                type: str
            kms_key_arn:
                description:
                - Not Provived.
                type: str
            sync_format:
                description:
                - Not Provived.
                type: str
        type: dict
    state:
        choices:
        - present
        - absent
        - list
        - describe
        - get
        default: present
        description:
        - Goal state for resource.
        - I(state=present) creates the resource if it doesn't exist, or updates to
            the provided state if the resource already exists.
        - I(state=absent) ensures an existing instance is deleted.
        - I(state=list) get all the existing resources.
        - I(state=describe) or I(state=get) retrieves information on an existing resource.
        type: str
    sync_format:
        description:
        - Not Provived.
        type: str
    sync_name:
        description:
        - Not Provived.
        type: str
    sync_source:
        description:
        - Not Provived.
        suboptions:
            aws_organizations_source:
                description:
                - Not Provived.
                suboptions:
                    organization_source_type:
                        description:
                        - Not Provived.
                        type: str
                    organizational_units:
                        description:
                        - Not Provived.
                        elements: str
                        type: list
                type: dict
            include_future_regions:
                description:
                - Not Provived.
                type: bool
            source_regions:
                description:
                - Not Provived.
                elements: str
                type: list
            source_type:
                description:
                - Not Provived.
                type: str
        type: dict
    sync_type:
        description:
        - Not Provived.
        type: str
    wait:
        default: false
        description:
        - Wait for operation to complete before returning.
        type: bool
    wait_timeout:
        default: 320
        description:
        - How many seconds to wait for an operation to complete before timing out.
        type: int
author: Ansible Cloud Team (@ansible-collections)
version_added: 0.3.0
extends_documentation_fragment:
- amazon.aws.aws
- amazon.aws.ec2
- amazon.cloud.boto3
"""

EXAMPLES = r"""
"""

RETURN = r"""
result:
    description:
        - When I(state=list), it is a list containing dictionaries of resource information.
        - Otherwise, it is a dictionary of resource information.
        - When I(state=absent), it is an empty dictionary.
    returned: always
    type: complex
    contains:
        identifier:
            description: The unique identifier of the resource.
            type: str
        properties:
            description: The resource properties.
            type: dict
"""


from ansible_collections.amazon.cloud.plugins.module_utils.core import (
    AnsibleAmazonCloudModule,
)
from ansible_collections.amazon.cloud.plugins.module_utils.core import (
    CloudControlResource,
)
from ansible_collections.amazon.cloud.plugins.module_utils.core import (
    snake_dict_to_camel_dict,
)
from ansible_collections.amazon.cloud.plugins.module_utils.core import (
    ansible_dict_to_boto3_tag_list,
)


def main():

    argument_spec = dict(
        state=dict(
            type="str",
            choices=["present", "absent", "list", "describe", "get"],
            default="present",
        ),
    )

    argument_spec["s3_destination"] = {
        "type": "dict",
        "options": {
            "kms_key_arn": {"type": "str"},
            "bucket_prefix": {"type": "str"},
            "bucket_name": {"type": "str"},
            "bucket_region": {"type": "str"},
            "sync_format": {"type": "str"},
        },
    }
    argument_spec["kms_key_arn"] = {"type": "str"}
    argument_spec["sync_source"] = {
        "type": "dict",
        "options": {
            "include_future_regions": {"type": "bool"},
            "source_regions": {"type": "list", "elements": "str"},
            "source_type": {"type": "str"},
            "aws_organizations_source": {
                "type": "dict",
                "options": {
                    "organizational_units": {"type": "list", "elements": "str"},
                    "organization_source_type": {"type": "str"},
                },
            },
        },
    }
    argument_spec["bucket_name"] = {"type": "str"}
    argument_spec["bucket_region"] = {"type": "str"}
    argument_spec["sync_format"] = {"type": "str"}
    argument_spec["sync_name"] = {"type": "str"}
    argument_spec["sync_type"] = {"type": "str"}
    argument_spec["bucket_prefix"] = {"type": "str"}
    argument_spec["state"] = {
        "type": "str",
        "choices": ["present", "absent", "list", "describe", "get"],
        "default": "present",
    }
    argument_spec["wait"] = {"type": "bool", "default": False}
    argument_spec["wait_timeout"] = {"type": "int", "default": 320}
    argument_spec["force"] = {"type": "bool", "default": False}

    required_if = [
        ["state", "present", ["sync_name"], True],
        ["state", "absent", ["sync_name"], True],
        ["state", "get", ["sync_name"], True],
    ]
    mutually_exclusive = []

    module = AnsibleAmazonCloudModule(
        argument_spec=argument_spec,
        required_if=required_if,
        mutually_exclusive=mutually_exclusive,
        supports_check_mode=True,
    )
    cloud = CloudControlResource(module)

    type_name = "AWS::SSM::ResourceDataSync"

    params = {}

    params["bucket_name"] = module.params.get("bucket_name")
    params["bucket_prefix"] = module.params.get("bucket_prefix")
    params["bucket_region"] = module.params.get("bucket_region")
    params["kms_key_arn"] = module.params.get("kms_key_arn")
    params["s3_destination"] = module.params.get("s3_destination")
    params["sync_format"] = module.params.get("sync_format")
    params["sync_name"] = module.params.get("sync_name")
    params["sync_source"] = module.params.get("sync_source")
    params["sync_type"] = module.params.get("sync_type")

    # The DesiredState we pass to AWS must be a JSONArray of non-null values
    _params_to_set = {k: v for k, v in params.items() if v is not None}

    # Only if resource is taggable
    if module.params.get("tags") is not None:
        _params_to_set["tags"] = ansible_dict_to_boto3_tag_list(module.params["tags"])

    params_to_set = snake_dict_to_camel_dict(_params_to_set, capitalize_first=True)

    # Ignore createOnlyProperties that can be set only during resource creation
    create_only_params = [
        "kms_key_arn",
        "sync_format",
        "bucket_prefix",
        "sync_name",
        "bucket_region",
        "bucket_name",
        "s3_destination",
        "sync_type",
    ]

    # Necessary to handle when module does not support all the states
    handlers = ["create", "delete", "update", "list", "read"]

    state = module.params.get("state")
    identifier = ["sync_name"]

    results = {"changed": False, "result": {}}

    if state == "list":
        if "list" not in handlers:
            module.exit_json(
                **results, msg=f"Resource type {type_name} cannot be listed."
            )
        results["result"] = cloud.list_resources(type_name, identifier)

    if state in ("describe", "get"):
        if "read" not in handlers:
            module.exit_json(
                **results, msg=f"Resource type {type_name} cannot be read."
            )
        results["result"] = cloud.get_resource(type_name, identifier)

    if state == "present":
        results = cloud.present(
            type_name, identifier, params_to_set, create_only_params
        )

    if state == "absent":
        results["changed"] |= cloud.absent(type_name, identifier)

    module.exit_json(**results)


if __name__ == "__main__":
    main()
