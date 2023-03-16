#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright: (c) 2021, Ansible Project
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# template: header.j2
# This module is autogenerated by vmware_rest_code_generator.
# See: https://github.com/ansible-collections/vmware_rest_code_generator
from __future__ import absolute_import, division, print_function

__metaclass__ = type


DOCUMENTATION = r"""
module: content_locallibrary_info
short_description: Returns a given local library.
description: Returns a given local library.
options:
    library_id:
        description:
        - Identifier of the local library to return. Required with I(state=['get'])
        type: str
    session_timeout:
        description:
        - 'Timeout settings for client session. '
        - 'The maximal number of seconds for the whole operation including connection
            establishment, request sending and response. '
        - The default value is 300s.
        type: float
        version_added: 2.1.0
    vcenter_hostname:
        description:
        - The hostname or IP address of the vSphere vCenter
        - If the value is not specified in the task, the value of environment variable
            C(VMWARE_HOST) will be used instead.
        required: true
        type: str
    vcenter_password:
        description:
        - The vSphere vCenter password
        - If the value is not specified in the task, the value of environment variable
            C(VMWARE_PASSWORD) will be used instead.
        required: true
        type: str
    vcenter_rest_log_file:
        description:
        - 'You can use this optional parameter to set the location of a log file. '
        - 'This file will be used to record the HTTP REST interaction. '
        - 'The file will be stored on the host that run the module. '
        - 'If the value is not specified in the task, the value of '
        - environment variable C(VMWARE_REST_LOG_FILE) will be used instead.
        type: str
    vcenter_username:
        description:
        - The vSphere vCenter username
        - If the value is not specified in the task, the value of environment variable
            C(VMWARE_USER) will be used instead.
        required: true
        type: str
    vcenter_validate_certs:
        default: true
        description:
        - Allows connection when SSL certificates are not valid. Set to C(false) when
            certificates are not trusted.
        - If the value is not specified in the task, the value of environment variable
            C(VMWARE_VALIDATE_CERTS) will be used instead.
        type: bool
author:
- Ansible Cloud Team (@ansible-collections)
version_added: 2.0.0
requirements:
- vSphere 7.0.2 or greater
- python >= 3.6
- aiohttp
notes:
- Tested on vSphere 7.0.2
"""

EXAMPLES = r"""
- name: List Local Content Library
  vmware.vmware_rest.content_locallibrary_info:
  register: my_content_library

- name: List all Local Content Library
  vmware.vmware_rest.content_locallibrary_info:
  register: all_content_libraries

- name: Create a new local content library
  vmware.vmware_rest.content_locallibrary:
    name: local_library_001
    description: automated
    publish_info:
      published: true
      authentication_method: NONE
    storage_backings:
    - datastore_id: "{{ lookup('vmware.vmware_rest.datastore_moid', '/my_dc/datastore/rw_datastore') }}"
      type: DATASTORE
    state: present
  register: ds_lib

- name: Retrieve the local content library information based upon id check mode
  vmware.vmware_rest.content_locallibrary_info:
    library_id: '{{ ds_lib.id }}'
  register: result
  check_mode: true
"""

RETURN = r"""
# content generated by the update_return_section callback# task: List all Local Content Library
value:
  description: List all Local Content Library
  returned: On success
  sample:
  - creation_time: '2022-11-23T20:02:22.940Z'
    description: automated
    id: a66d5c73-57f8-4a3a-9361-292a55f68516
    last_modified_time: '2022-11-23T20:02:22.940Z'
    name: my_library_on_nfs
    publish_info:
      authentication_method: NONE
      persist_json_enabled: 0
      publish_url: https://vcenter.test:443/cls/vcsp/lib/a66d5c73-57f8-4a3a-9361-292a55f68516/lib.json
      published: 1
      user_name: vcsp
    server_guid: 52fb0b5e-ffc3-465b-bf4f-e4e6d5423cf5
    storage_backings:
    - storage_uri: nfs://datastore.test/srv/share/content-library
      type: OTHER
    type: LOCAL
    version: '2'
  - creation_time: '2022-11-23T20:02:25.134Z'
    description: automated
    id: 3393956a-43ed-4e7f-bd96-eb39bd604445
    last_modified_time: '2022-11-23T20:02:25.134Z'
    name: my_library_on_nfs_0
    publish_info:
      authentication_method: NONE
      persist_json_enabled: 0
      publish_url: https://vcenter.test:443/cls/vcsp/lib/3393956a-43ed-4e7f-bd96-eb39bd604445/lib.json
      published: 1
      user_name: vcsp
    server_guid: 52fb0b5e-ffc3-465b-bf4f-e4e6d5423cf5
    storage_backings:
    - storage_uri: nfs://datastore.test/srv/share/content-library
      type: OTHER
    type: LOCAL
    version: '2'
  - creation_time: '2022-11-23T20:02:26.342Z'
    description: automated
    id: 87f66f86-c046-45a7-9563-d59ea220babf
    last_modified_time: '2022-11-23T20:02:26.342Z'
    name: my_library_on_nfs_1
    publish_info:
      authentication_method: NONE
      persist_json_enabled: 0
      publish_url: https://vcenter.test:443/cls/vcsp/lib/87f66f86-c046-45a7-9563-d59ea220babf/lib.json
      published: 1
      user_name: vcsp
    server_guid: 52fb0b5e-ffc3-465b-bf4f-e4e6d5423cf5
    storage_backings:
    - storage_uri: nfs://datastore.test/srv/share/content-library
      type: OTHER
    type: LOCAL
    version: '2'
  - creation_time: '2022-11-23T20:02:27.504Z'
    description: automated
    id: f6c590c4-ae6d-4ad0-9362-378196e98a3c
    last_modified_time: '2022-11-23T20:02:27.504Z'
    name: my_library_on_nfs_2
    publish_info:
      authentication_method: NONE
      persist_json_enabled: 0
      publish_url: https://vcenter.test:443/cls/vcsp/lib/f6c590c4-ae6d-4ad0-9362-378196e98a3c/lib.json
      published: 1
      user_name: vcsp
    server_guid: 52fb0b5e-ffc3-465b-bf4f-e4e6d5423cf5
    storage_backings:
    - storage_uri: nfs://datastore.test/srv/share/content-library
      type: OTHER
    type: LOCAL
    version: '2'
  - creation_time: '2022-11-23T20:02:28.821Z'
    description: automated
    id: e8917499-2a4c-4b70-b39b-ae0caaef89c3
    last_modified_time: '2022-11-23T20:02:28.821Z'
    name: my_library_on_nfs_3
    publish_info:
      authentication_method: NONE
      persist_json_enabled: 0
      publish_url: https://vcenter.test:443/cls/vcsp/lib/e8917499-2a4c-4b70-b39b-ae0caaef89c3/lib.json
      published: 1
      user_name: vcsp
    server_guid: 52fb0b5e-ffc3-465b-bf4f-e4e6d5423cf5
    storage_backings:
    - storage_uri: nfs://datastore.test/srv/share/content-library
      type: OTHER
    type: LOCAL
    version: '2'
  - creation_time: '2022-11-23T20:02:30.085Z'
    description: automated
    id: 630ebdfe-8913-45d3-aaa8-9c2fdecbb76b
    last_modified_time: '2022-11-23T20:02:30.085Z'
    name: my_library_on_nfs_4
    publish_info:
      authentication_method: NONE
      persist_json_enabled: 0
      publish_url: https://vcenter.test:443/cls/vcsp/lib/630ebdfe-8913-45d3-aaa8-9c2fdecbb76b/lib.json
      published: 1
      user_name: vcsp
    server_guid: 52fb0b5e-ffc3-465b-bf4f-e4e6d5423cf5
    storage_backings:
    - storage_uri: nfs://datastore.test/srv/share/content-library
      type: OTHER
    type: LOCAL
    version: '2'
  - creation_time: '2022-11-23T20:02:31.482Z'
    description: automated
    id: a046e2e5-bd55-4d04-9443-750a2ab35a6d
    last_modified_time: '2022-11-23T20:02:31.482Z'
    name: my_library_on_nfs_5
    publish_info:
      authentication_method: NONE
      persist_json_enabled: 0
      publish_url: https://vcenter.test:443/cls/vcsp/lib/a046e2e5-bd55-4d04-9443-750a2ab35a6d/lib.json
      published: 1
      user_name: vcsp
    server_guid: 52fb0b5e-ffc3-465b-bf4f-e4e6d5423cf5
    storage_backings:
    - storage_uri: nfs://datastore.test/srv/share/content-library
      type: OTHER
    type: LOCAL
    version: '2'
  - creation_time: '2022-11-23T20:02:32.846Z'
    description: automated
    id: b94383b1-7877-4dbd-8c33-51abc39451ff
    last_modified_time: '2022-11-23T20:02:32.846Z'
    name: my_library_on_nfs_6
    publish_info:
      authentication_method: NONE
      persist_json_enabled: 0
      publish_url: https://vcenter.test:443/cls/vcsp/lib/b94383b1-7877-4dbd-8c33-51abc39451ff/lib.json
      published: 1
      user_name: vcsp
    server_guid: 52fb0b5e-ffc3-465b-bf4f-e4e6d5423cf5
    storage_backings:
    - storage_uri: nfs://datastore.test/srv/share/content-library
      type: OTHER
    type: LOCAL
    version: '2'
  - creation_time: '2022-11-23T20:02:34.218Z'
    description: automated
    id: 8e3efb68-cb84-4ce0-a65a-6c94cc6e6e00
    last_modified_time: '2022-11-23T20:02:34.218Z'
    name: my_library_on_nfs_7
    publish_info:
      authentication_method: NONE
      persist_json_enabled: 0
      publish_url: https://vcenter.test:443/cls/vcsp/lib/8e3efb68-cb84-4ce0-a65a-6c94cc6e6e00/lib.json
      published: 1
      user_name: vcsp
    server_guid: 52fb0b5e-ffc3-465b-bf4f-e4e6d5423cf5
    storage_backings:
    - storage_uri: nfs://datastore.test/srv/share/content-library
      type: OTHER
    type: LOCAL
    version: '2'
  - creation_time: '2022-11-23T20:02:35.922Z'
    description: automated
    id: 0b12c0b3-6c6d-448d-9033-e054a70183e7
    last_modified_time: '2022-11-23T20:02:35.922Z'
    name: my_library_on_nfs_8
    publish_info:
      authentication_method: NONE
      persist_json_enabled: 0
      publish_url: https://vcenter.test:443/cls/vcsp/lib/0b12c0b3-6c6d-448d-9033-e054a70183e7/lib.json
      published: 1
      user_name: vcsp
    server_guid: 52fb0b5e-ffc3-465b-bf4f-e4e6d5423cf5
    storage_backings:
    - storage_uri: nfs://datastore.test/srv/share/content-library
      type: OTHER
    type: LOCAL
    version: '2'
  - creation_time: '2022-11-23T20:02:37.796Z'
    description: automated
    id: 46454797-bbe0-415a-9fe9-3cf2f74a14db
    last_modified_time: '2022-11-23T20:02:37.796Z'
    name: my_library_on_nfs_9
    publish_info:
      authentication_method: NONE
      persist_json_enabled: 0
      publish_url: https://vcenter.test:443/cls/vcsp/lib/46454797-bbe0-415a-9fe9-3cf2f74a14db/lib.json
      published: 1
      user_name: vcsp
    server_guid: 52fb0b5e-ffc3-465b-bf4f-e4e6d5423cf5
    storage_backings:
    - storage_uri: nfs://datastore.test/srv/share/content-library
      type: OTHER
    type: LOCAL
    version: '2'
  - creation_time: '2022-11-23T20:02:38.976Z'
    description: automated
    id: 209926aa-e3fe-46a5-95f2-501e82a5139b
    last_modified_time: '2022-11-23T20:02:38.976Z'
    name: my_library_on_nfs_10
    publish_info:
      authentication_method: NONE
      persist_json_enabled: 0
      publish_url: https://vcenter.test:443/cls/vcsp/lib/209926aa-e3fe-46a5-95f2-501e82a5139b/lib.json
      published: 1
      user_name: vcsp
    server_guid: 52fb0b5e-ffc3-465b-bf4f-e4e6d5423cf5
    storage_backings:
    - storage_uri: nfs://datastore.test/srv/share/content-library
      type: OTHER
    type: LOCAL
    version: '2'
  type: list
"""

# This structure describes the format of the data expected by the end-points
PAYLOAD_FORMAT = {
    "get": {"query": {}, "body": {}, "path": {"library_id": "library_id"}},
    "list": {"query": {}, "body": {}, "path": {}},
}  # pylint: disable=line-too-long

import json
import socket
from ansible.module_utils.basic import env_fallback

try:
    from ansible_collections.cloud.common.plugins.module_utils.turbo.exceptions import (
        EmbeddedModuleFailure,
    )
    from ansible_collections.cloud.common.plugins.module_utils.turbo.module import (
        AnsibleTurboModule as AnsibleModule,
    )

    AnsibleModule.collection_name = "vmware.vmware_rest"
except ImportError:
    from ansible.module_utils.basic import AnsibleModule
from ansible_collections.vmware.vmware_rest.plugins.module_utils.vmware_rest import (
    build_full_device_list,
    exists,
    gen_args,
    get_device_info,
    get_subdevice_type,
    list_devices,
    open_session,
    prepare_payload,
    update_changed_flag,
    session_timeout,
)


def prepare_argument_spec():
    argument_spec = {
        "vcenter_hostname": dict(
            type="str", required=True, fallback=(env_fallback, ["VMWARE_HOST"]),
        ),
        "vcenter_username": dict(
            type="str", required=True, fallback=(env_fallback, ["VMWARE_USER"]),
        ),
        "vcenter_password": dict(
            type="str",
            required=True,
            no_log=True,
            fallback=(env_fallback, ["VMWARE_PASSWORD"]),
        ),
        "vcenter_validate_certs": dict(
            type="bool",
            required=False,
            default=True,
            fallback=(env_fallback, ["VMWARE_VALIDATE_CERTS"]),
        ),
        "vcenter_rest_log_file": dict(
            type="str",
            required=False,
            fallback=(env_fallback, ["VMWARE_REST_LOG_FILE"]),
        ),
        "session_timeout": dict(
            type="float",
            required=False,
            fallback=(env_fallback, ["VMWARE_SESSION_TIMEOUT"]),
        ),
    }

    argument_spec["library_id"] = {"type": "str"}

    return argument_spec


async def main():
    required_if = list([])

    module_args = prepare_argument_spec()
    module = AnsibleModule(
        argument_spec=module_args, required_if=required_if, supports_check_mode=True
    )
    if not module.params["vcenter_hostname"]:
        module.fail_json("vcenter_hostname cannot be empty")
    if not module.params["vcenter_username"]:
        module.fail_json("vcenter_username cannot be empty")
    if not module.params["vcenter_password"]:
        module.fail_json("vcenter_password cannot be empty")
    try:
        session = await open_session(
            vcenter_hostname=module.params["vcenter_hostname"],
            vcenter_username=module.params["vcenter_username"],
            vcenter_password=module.params["vcenter_password"],
            validate_certs=module.params["vcenter_validate_certs"],
            log_file=module.params["vcenter_rest_log_file"],
        )
    except EmbeddedModuleFailure as err:
        module.fail_json(err.get_message())
    result = await entry_point(module, session)
    module.exit_json(**result)


# template: info_list_and_get_module.j2
def build_url(params):
    import yarl

    if params.get("library_id"):
        _in_query_parameters = PAYLOAD_FORMAT["get"]["query"].keys()
        return yarl.URL(
            ("https://{vcenter_hostname}" "/api/content/local-library/").format(
                **params
            )
            + params["library_id"]
            + gen_args(params, _in_query_parameters),
            encoded=True,
        )
    _in_query_parameters = PAYLOAD_FORMAT["list"]["query"].keys()
    return yarl.URL(
        ("https://{vcenter_hostname}" "/api/content/local-library").format(**params)
        + gen_args(params, _in_query_parameters),
        encoded=True,
    )


async def entry_point(module, session):
    url = build_url(module.params)
    async with session.get(url, **session_timeout(module.params)) as resp:
        _json = await resp.json()

        if "value" not in _json:  # 7.0.2+
            _json = {"value": _json}

        if module.params.get("library_id"):
            _json["id"] = module.params.get("library_id")
        elif module.params.get("label"):  # TODO extend the list of filter
            _json = await exists(module.params, session, str(url))
        elif (
            isinstance(_json["value"], list)
            and len(_json["value"]) > 0
            and isinstance(_json["value"][0], str)
        ):
            # this is a list of id, we fetch the details
            full_device_list = await build_full_device_list(session, str(url), _json)
            _json = {"value": [i["value"] for i in full_device_list]}

        return await update_changed_flag(_json, resp.status, "get")


if __name__ == "__main__":
    import asyncio

    current_loop = asyncio.get_event_loop_policy().get_event_loop()
    current_loop.run_until_complete(main())
