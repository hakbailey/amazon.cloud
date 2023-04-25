#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright: (c) 2022, Ansible Project
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# template: header.j2
# This module is autogenerated using the gouttelette generator tool
# See: https://github.com/ansible-collections/gouttelette


DOCUMENTATION = r"""
module: ecr_repository
short_description: Creates and manages an AWS ECR Repository resource
description:
- The AWS ECR Repository resource specifies an Amazon Elastic Container Registry (Amazon
    ECR) repository, where users can push and pull Docker images, Open Container Initiative
    (OCI) images, and OCI compatible artifacts.
- For more information see U(https://docs.aws.amazon.com/AmazonECR/latest/userguide/Repositories.html).
options:
    encryption_configuration:
        description:
        - The encryption configuration for the repository.
        - This determines how the contents of your repository are encrypted at rest.
        - By default, when no encryption configuration is set or the C(AES256) encryption
            type is used, Amazon ECR uses server-side encryption with Amazon S3-managed
            encryption keys which encrypts your data at rest using an AES-256 encryption
            algorithm.
        - This does not require any action on your part.
        - For more information, see U(https://docs.aws.amazon.com/AmazonECR/latest/userguide/encryption-at-rest.html).
        suboptions:
            encryption_type:
                choices:
                - AES256
                - KMS
                description:
                - The encryption type to use.
                type: str
            kms_key:
                description:
                - If you use the C(KMS) encryption type, specify the CMK to use for
                    encryption.
                - The alias, key ID, or full ARN of the CMK can be specified.
                - The key must exist in the same Region as the repository.
                - If no key is specified, the default AWS managed CMK for Amazon ECR
                    will be used.
                type: str
        type: dict
    force:
        default: false
        description:
        - Cancel IN_PROGRESS and PENDING resource requestes.
        - Because you can only perform a single operation on a given resource at a
            time, there might be cases where you need to cancel the current resource
            operation to make the resource available so that another operation may
            be performed on it.
        type: bool
    image_scanning_configuration:
        description:
        - The image scanning configuration for the repository.
        - This setting determines whether images are scanned for known vulnerabilities
            after being pushed to the repository.
        suboptions:
            scan_on_push:
                description:
                - The setting that determines whether images are scanned after being
                    pushed to a repository.
                type: bool
        type: dict
    image_tag_mutability:
        choices:
        - IMMUTABLE
        - MUTABLE
        description:
        - The image tag mutability setting for the repository.
        type: str
    lifecycle_policy:
        description:
        - The I(lifecycle_policy) property type specifies a lifecycle policy.
        - For information about lifecycle policy syntax, see U(https://docs.aws.amazon.com/AmazonECR/latest/userguide/LifecyclePolicies.html).
        suboptions:
            lifecycle_policy_text:
                description:
                - The JSON repository policy text to apply to the repository.
                type: str
            registry_id:
                description:
                - The AWS account ID associated with the registry that contains the
                    repository.
                - If you do not specify a registry, the default registry is assumed.
                type: str
        type: dict
    purge_tags:
        default: true
        description:
        - Remove tags not listed in I(tags).
        type: bool
    repository_name:
        description:
        - The name to use for the repository.
        - The repository name may be specified on its own (such as nginx-web-app)
            or it can be prepended with a namespace to group the repository into a
            category (such as project-a/nginx-web-app).
        - If you dont specify a name, AWS CloudFormation generates a unique physical
            ID and uses that ID for the repository name.
        - For more information, see U(https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-name.html.).
        type: str
    repository_policy_text:
        description:
        - The JSON repository policy text to apply to the repository.
        - For more information, see U(https://docs.aws.amazon.com/AmazonECR/latest/userguide/RepositoryPolicyExamples.html)
            in the Amazon Elastic Container Registry User Guide.
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
    tags:
        aliases:
        - resource_tags
        description:
        - A dict of tags to apply to the resource.
        - To remove all tags set I(tags={}) and I(purge_tags=true).
        type: dict
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

    argument_spec["lifecycle_policy"] = {
        "type": "dict",
        "options": {
            "lifecycle_policy_text": {"type": "str"},
            "registry_id": {"type": "str"},
        },
    }
    argument_spec["repository_name"] = {"type": "str"}
    argument_spec["repository_policy_text"] = {"type": "dict"}
    argument_spec["tags"] = {"type": "dict", "aliases": ["resource_tags"]}
    argument_spec["image_tag_mutability"] = {
        "type": "str",
        "choices": ["IMMUTABLE", "MUTABLE"],
    }
    argument_spec["image_scanning_configuration"] = {
        "type": "dict",
        "options": {"scan_on_push": {"type": "bool"}},
    }
    argument_spec["encryption_configuration"] = {
        "type": "dict",
        "options": {
            "encryption_type": {"type": "str", "choices": ["AES256", "KMS"]},
            "kms_key": {"type": "str"},
        },
    }
    argument_spec["state"] = {
        "type": "str",
        "choices": ["present", "absent", "list", "describe", "get"],
        "default": "present",
    }
    argument_spec["wait"] = {"type": "bool", "default": False}
    argument_spec["wait_timeout"] = {"type": "int", "default": 320}
    argument_spec["force"] = {"type": "bool", "default": False}
    argument_spec["purge_tags"] = {"type": "bool", "default": True}

    required_if = [
        ["state", "present", ["repository_name"], True],
        ["state", "absent", ["repository_name"], True],
        ["state", "get", ["repository_name"], True],
    ]
    mutually_exclusive = []

    module = AnsibleAmazonCloudModule(
        argument_spec=argument_spec,
        required_if=required_if,
        mutually_exclusive=mutually_exclusive,
        supports_check_mode=True,
    )
    cloud = CloudControlResource(module)

    type_name = "AWS::ECR::Repository"

    params = {}

    params["encryption_configuration"] = module.params.get("encryption_configuration")
    params["image_scanning_configuration"] = module.params.get(
        "image_scanning_configuration"
    )
    params["image_tag_mutability"] = module.params.get("image_tag_mutability")
    params["lifecycle_policy"] = module.params.get("lifecycle_policy")
    params["repository_name"] = module.params.get("repository_name")
    params["repository_policy_text"] = module.params.get("repository_policy_text")
    params["tags"] = module.params.get("tags")

    # The DesiredState we pass to AWS must be a JSONArray of non-null values
    _params_to_set = {k: v for k, v in params.items() if v is not None}

    # Only if resource is taggable
    if module.params.get("tags") is not None:
        _params_to_set["tags"] = ansible_dict_to_boto3_tag_list(module.params["tags"])

    params_to_set = snake_dict_to_camel_dict(_params_to_set, capitalize_first=True)

    # Ignore createOnlyProperties that can be set only during resource creation
    create_only_params = [
        "repository_name",
        "encryption_configuration",
        "encryption_type",
        "kms_key",
    ]

    # Necessary to handle when module does not support all the states
    handlers = ["create", "read", "update", "delete", "list"]

    state = module.params.get("state")
    identifier = ["repository_name"]

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
