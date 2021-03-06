"""Generated client library for bigtableadmin version v2."""
# NOTE: This file is autogenerated and should not be edited by hand.
from apitools.base.py import base_api
from googlecloudsdk.third_party.apis.bigtableadmin.v2 import bigtableadmin_v2_messages as messages


class BigtableadminV2(base_api.BaseApiClient):
  """Generated client library for service bigtableadmin version v2."""

  MESSAGES_MODULE = messages
  BASE_URL = u'https://bigtableadmin.googleapis.com/'

  _PACKAGE = u'bigtableadmin'
  _SCOPES = [u'https://www.googleapis.com/auth/cloud-platform', u'https://www.googleapis.com/auth/cloud-platform.read-only']
  _VERSION = u'v2'
  _CLIENT_ID = '1042881264118.apps.googleusercontent.com'
  _CLIENT_SECRET = 'x_Tw5K8nnjoRAqULM9PFAC2b'
  _USER_AGENT = 'x_Tw5K8nnjoRAqULM9PFAC2b'
  _CLIENT_CLASS_NAME = u'BigtableadminV2'
  _URL_VERSION = u'v2'
  _API_KEY = None

  def __init__(self, url='', credentials=None,
               get_credentials=True, http=None, model=None,
               log_request=False, log_response=False,
               credentials_args=None, default_global_params=None,
               additional_http_headers=None):
    """Create a new bigtableadmin handle."""
    url = url or self.BASE_URL
    super(BigtableadminV2, self).__init__(
        url, credentials=credentials,
        get_credentials=get_credentials, http=http, model=model,
        log_request=log_request, log_response=log_response,
        credentials_args=credentials_args,
        default_global_params=default_global_params,
        additional_http_headers=additional_http_headers)
    self.operations = self.OperationsService(self)
    self.projects_instances_clusters = self.ProjectsInstancesClustersService(self)
    self.projects_instances_tables = self.ProjectsInstancesTablesService(self)
    self.projects_instances = self.ProjectsInstancesService(self)
    self.projects = self.ProjectsService(self)

  class OperationsService(base_api.BaseApiService):
    """Service class for the operations resource."""

    _NAME = u'operations'

    def __init__(self, client):
      super(BigtableadminV2.OperationsService, self).__init__(client)
      self._upload_configs = {
          }

    def Cancel(self, request, global_params=None):
      """Starts asynchronous cancellation on a long-running operation.  The server.
makes a best effort to cancel the operation, but success is not
guaranteed.  If the server doesn't support this method, it returns
`google.rpc.Code.UNIMPLEMENTED`.  Clients can use
Operations.GetOperation or
other methods to check whether the cancellation succeeded or whether the
operation completed despite cancellation. On successful cancellation,
the operation is not deleted; instead, it becomes an operation with
an Operation.error value with a google.rpc.Status.code of 1,
corresponding to `Code.CANCELLED`.

      Args:
        request: (BigtableadminOperationsCancelRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Empty) The response message.
      """
      config = self.GetMethodConfig('Cancel')
      return self._RunMethod(
          config, request, global_params=global_params)

    Cancel.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v2/operations/{operationsId}:cancel',
        http_method=u'POST',
        method_id=u'bigtableadmin.operations.cancel',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[],
        relative_path=u'v2/{+name}:cancel',
        request_field='',
        request_type_name=u'BigtableadminOperationsCancelRequest',
        response_type_name=u'Empty',
        supports_download=False,
    )

    def Delete(self, request, global_params=None):
      """Deletes a long-running operation. This method indicates that the client is.
no longer interested in the operation result. It does not cancel the
operation. If the server doesn't support this method, it returns
`google.rpc.Code.UNIMPLEMENTED`.

      Args:
        request: (BigtableadminOperationsDeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Empty) The response message.
      """
      config = self.GetMethodConfig('Delete')
      return self._RunMethod(
          config, request, global_params=global_params)

    Delete.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v2/operations/{operationsId}',
        http_method=u'DELETE',
        method_id=u'bigtableadmin.operations.delete',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[],
        relative_path=u'v2/{+name}',
        request_field='',
        request_type_name=u'BigtableadminOperationsDeleteRequest',
        response_type_name=u'Empty',
        supports_download=False,
    )

    def Get(self, request, global_params=None):
      """Gets the latest state of a long-running operation.  Clients can use this.
method to poll the operation result at intervals as recommended by the API
service.

      Args:
        request: (BigtableadminOperationsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v2/operations/{operationsId}',
        http_method=u'GET',
        method_id=u'bigtableadmin.operations.get',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[],
        relative_path=u'v2/{+name}',
        request_field='',
        request_type_name=u'BigtableadminOperationsGetRequest',
        response_type_name=u'Operation',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      """Lists operations that match the specified filter in the request. If the.
server doesn't support this method, it returns `UNIMPLEMENTED`.

NOTE: the `name` binding below allows API services to override the binding
to use different resource name schemes, such as `users/*/operations`.

      Args:
        request: (BigtableadminOperationsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListOperationsResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v2/operations',
        http_method=u'GET',
        method_id=u'bigtableadmin.operations.list',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[u'filter', u'pageSize', u'pageToken'],
        relative_path=u'v2/{+name}',
        request_field='',
        request_type_name=u'BigtableadminOperationsListRequest',
        response_type_name=u'ListOperationsResponse',
        supports_download=False,
    )

  class ProjectsInstancesClustersService(base_api.BaseApiService):
    """Service class for the projects_instances_clusters resource."""

    _NAME = u'projects_instances_clusters'

    def __init__(self, client):
      super(BigtableadminV2.ProjectsInstancesClustersService, self).__init__(client)
      self._upload_configs = {
          }

    def Create(self, request, global_params=None):
      """Creates a cluster within an instance.

      Args:
        request: (BigtableadminProjectsInstancesClustersCreateRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Create')
      return self._RunMethod(
          config, request, global_params=global_params)

    Create.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v2/projects/{projectsId}/instances/{instancesId}/clusters',
        http_method=u'POST',
        method_id=u'bigtableadmin.projects.instances.clusters.create',
        ordered_params=[u'parent'],
        path_params=[u'parent'],
        query_params=[u'clusterId'],
        relative_path=u'v2/{+parent}/clusters',
        request_field=u'cluster',
        request_type_name=u'BigtableadminProjectsInstancesClustersCreateRequest',
        response_type_name=u'Operation',
        supports_download=False,
    )

    def Delete(self, request, global_params=None):
      """Deletes a cluster from an instance.

      Args:
        request: (BigtableadminProjectsInstancesClustersDeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Empty) The response message.
      """
      config = self.GetMethodConfig('Delete')
      return self._RunMethod(
          config, request, global_params=global_params)

    Delete.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v2/projects/{projectsId}/instances/{instancesId}/clusters/{clustersId}',
        http_method=u'DELETE',
        method_id=u'bigtableadmin.projects.instances.clusters.delete',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[],
        relative_path=u'v2/{+name}',
        request_field='',
        request_type_name=u'BigtableadminProjectsInstancesClustersDeleteRequest',
        response_type_name=u'Empty',
        supports_download=False,
    )

    def Get(self, request, global_params=None):
      """Gets information about a cluster.

      Args:
        request: (BigtableadminProjectsInstancesClustersGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Cluster) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v2/projects/{projectsId}/instances/{instancesId}/clusters/{clustersId}',
        http_method=u'GET',
        method_id=u'bigtableadmin.projects.instances.clusters.get',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[],
        relative_path=u'v2/{+name}',
        request_field='',
        request_type_name=u'BigtableadminProjectsInstancesClustersGetRequest',
        response_type_name=u'Cluster',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      """Lists information about clusters in an instance.

      Args:
        request: (BigtableadminProjectsInstancesClustersListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListClustersResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v2/projects/{projectsId}/instances/{instancesId}/clusters',
        http_method=u'GET',
        method_id=u'bigtableadmin.projects.instances.clusters.list',
        ordered_params=[u'parent'],
        path_params=[u'parent'],
        query_params=[u'pageToken'],
        relative_path=u'v2/{+parent}/clusters',
        request_field='',
        request_type_name=u'BigtableadminProjectsInstancesClustersListRequest',
        response_type_name=u'ListClustersResponse',
        supports_download=False,
    )

    def Update(self, request, global_params=None):
      """Updates a cluster within an instance.

      Args:
        request: (Cluster) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Update')
      return self._RunMethod(
          config, request, global_params=global_params)

    Update.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v2/projects/{projectsId}/instances/{instancesId}/clusters/{clustersId}',
        http_method=u'PUT',
        method_id=u'bigtableadmin.projects.instances.clusters.update',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[],
        relative_path=u'v2/{+name}',
        request_field='<request>',
        request_type_name=u'Cluster',
        response_type_name=u'Operation',
        supports_download=False,
    )

  class ProjectsInstancesTablesService(base_api.BaseApiService):
    """Service class for the projects_instances_tables resource."""

    _NAME = u'projects_instances_tables'

    def __init__(self, client):
      super(BigtableadminV2.ProjectsInstancesTablesService, self).__init__(client)
      self._upload_configs = {
          }

    def Create(self, request, global_params=None):
      """Creates a new table in the specified instance.
The table can be created with a full set of initial column families,
specified in the request.

      Args:
        request: (BigtableadminProjectsInstancesTablesCreateRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Table) The response message.
      """
      config = self.GetMethodConfig('Create')
      return self._RunMethod(
          config, request, global_params=global_params)

    Create.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v2/projects/{projectsId}/instances/{instancesId}/tables',
        http_method=u'POST',
        method_id=u'bigtableadmin.projects.instances.tables.create',
        ordered_params=[u'parent'],
        path_params=[u'parent'],
        query_params=[],
        relative_path=u'v2/{+parent}/tables',
        request_field=u'createTableRequest',
        request_type_name=u'BigtableadminProjectsInstancesTablesCreateRequest',
        response_type_name=u'Table',
        supports_download=False,
    )

    def Delete(self, request, global_params=None):
      """Permanently deletes a specified table and all of its data.

      Args:
        request: (BigtableadminProjectsInstancesTablesDeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Empty) The response message.
      """
      config = self.GetMethodConfig('Delete')
      return self._RunMethod(
          config, request, global_params=global_params)

    Delete.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v2/projects/{projectsId}/instances/{instancesId}/tables/{tablesId}',
        http_method=u'DELETE',
        method_id=u'bigtableadmin.projects.instances.tables.delete',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[],
        relative_path=u'v2/{+name}',
        request_field='',
        request_type_name=u'BigtableadminProjectsInstancesTablesDeleteRequest',
        response_type_name=u'Empty',
        supports_download=False,
    )

    def DropRowRange(self, request, global_params=None):
      """Permanently drop/delete a row range from a specified table. The request can.
specify whether to delete all rows in a table, or only those that match a
particular prefix.

      Args:
        request: (BigtableadminProjectsInstancesTablesDropRowRangeRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Empty) The response message.
      """
      config = self.GetMethodConfig('DropRowRange')
      return self._RunMethod(
          config, request, global_params=global_params)

    DropRowRange.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v2/projects/{projectsId}/instances/{instancesId}/tables/{tablesId}:dropRowRange',
        http_method=u'POST',
        method_id=u'bigtableadmin.projects.instances.tables.dropRowRange',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[],
        relative_path=u'v2/{+name}:dropRowRange',
        request_field=u'dropRowRangeRequest',
        request_type_name=u'BigtableadminProjectsInstancesTablesDropRowRangeRequest',
        response_type_name=u'Empty',
        supports_download=False,
    )

    def Get(self, request, global_params=None):
      """Gets metadata information about the specified table.

      Args:
        request: (BigtableadminProjectsInstancesTablesGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Table) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v2/projects/{projectsId}/instances/{instancesId}/tables/{tablesId}',
        http_method=u'GET',
        method_id=u'bigtableadmin.projects.instances.tables.get',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[u'view'],
        relative_path=u'v2/{+name}',
        request_field='',
        request_type_name=u'BigtableadminProjectsInstancesTablesGetRequest',
        response_type_name=u'Table',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      """Lists all tables served from a specified instance.

      Args:
        request: (BigtableadminProjectsInstancesTablesListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListTablesResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v2/projects/{projectsId}/instances/{instancesId}/tables',
        http_method=u'GET',
        method_id=u'bigtableadmin.projects.instances.tables.list',
        ordered_params=[u'parent'],
        path_params=[u'parent'],
        query_params=[u'pageToken', u'view'],
        relative_path=u'v2/{+parent}/tables',
        request_field='',
        request_type_name=u'BigtableadminProjectsInstancesTablesListRequest',
        response_type_name=u'ListTablesResponse',
        supports_download=False,
    )

    def ModifyColumnFamilies(self, request, global_params=None):
      """Atomically performs a series of column family modifications.
on the specified table.

      Args:
        request: (BigtableadminProjectsInstancesTablesModifyColumnFamiliesRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Table) The response message.
      """
      config = self.GetMethodConfig('ModifyColumnFamilies')
      return self._RunMethod(
          config, request, global_params=global_params)

    ModifyColumnFamilies.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v2/projects/{projectsId}/instances/{instancesId}/tables/{tablesId}:modifyColumnFamilies',
        http_method=u'POST',
        method_id=u'bigtableadmin.projects.instances.tables.modifyColumnFamilies',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[],
        relative_path=u'v2/{+name}:modifyColumnFamilies',
        request_field=u'modifyColumnFamiliesRequest',
        request_type_name=u'BigtableadminProjectsInstancesTablesModifyColumnFamiliesRequest',
        response_type_name=u'Table',
        supports_download=False,
    )

  class ProjectsInstancesService(base_api.BaseApiService):
    """Service class for the projects_instances resource."""

    _NAME = u'projects_instances'

    def __init__(self, client):
      super(BigtableadminV2.ProjectsInstancesService, self).__init__(client)
      self._upload_configs = {
          }

    def Create(self, request, global_params=None):
      """Create an instance within a project.

      Args:
        request: (CreateInstanceRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Create')
      return self._RunMethod(
          config, request, global_params=global_params)

    Create.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v2/projects/{projectsId}/instances',
        http_method=u'POST',
        method_id=u'bigtableadmin.projects.instances.create',
        ordered_params=[u'parent'],
        path_params=[u'parent'],
        query_params=[],
        relative_path=u'v2/{+parent}/instances',
        request_field='<request>',
        request_type_name=u'CreateInstanceRequest',
        response_type_name=u'Operation',
        supports_download=False,
    )

    def Delete(self, request, global_params=None):
      """Delete an instance from a project.

      Args:
        request: (BigtableadminProjectsInstancesDeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Empty) The response message.
      """
      config = self.GetMethodConfig('Delete')
      return self._RunMethod(
          config, request, global_params=global_params)

    Delete.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v2/projects/{projectsId}/instances/{instancesId}',
        http_method=u'DELETE',
        method_id=u'bigtableadmin.projects.instances.delete',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[],
        relative_path=u'v2/{+name}',
        request_field='',
        request_type_name=u'BigtableadminProjectsInstancesDeleteRequest',
        response_type_name=u'Empty',
        supports_download=False,
    )

    def Get(self, request, global_params=None):
      """Gets information about an instance.

      Args:
        request: (BigtableadminProjectsInstancesGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Instance) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v2/projects/{projectsId}/instances/{instancesId}',
        http_method=u'GET',
        method_id=u'bigtableadmin.projects.instances.get',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[],
        relative_path=u'v2/{+name}',
        request_field='',
        request_type_name=u'BigtableadminProjectsInstancesGetRequest',
        response_type_name=u'Instance',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      """Lists information about instances in a project.

      Args:
        request: (BigtableadminProjectsInstancesListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListInstancesResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v2/projects/{projectsId}/instances',
        http_method=u'GET',
        method_id=u'bigtableadmin.projects.instances.list',
        ordered_params=[u'parent'],
        path_params=[u'parent'],
        query_params=[u'pageToken'],
        relative_path=u'v2/{+parent}/instances',
        request_field='',
        request_type_name=u'BigtableadminProjectsInstancesListRequest',
        response_type_name=u'ListInstancesResponse',
        supports_download=False,
    )

    def Update(self, request, global_params=None):
      """Updates an instance within a project.

      Args:
        request: (Instance) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Instance) The response message.
      """
      config = self.GetMethodConfig('Update')
      return self._RunMethod(
          config, request, global_params=global_params)

    Update.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v2/projects/{projectsId}/instances/{instancesId}',
        http_method=u'PUT',
        method_id=u'bigtableadmin.projects.instances.update',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[],
        relative_path=u'v2/{+name}',
        request_field='<request>',
        request_type_name=u'Instance',
        response_type_name=u'Instance',
        supports_download=False,
    )

  class ProjectsService(base_api.BaseApiService):
    """Service class for the projects resource."""

    _NAME = u'projects'

    def __init__(self, client):
      super(BigtableadminV2.ProjectsService, self).__init__(client)
      self._upload_configs = {
          }
