function redirectHome(collapseId) {

    window.location = location.href;
}



function addProcess() {

    var data = {
        "processname": $('#ProcessName').val(),
        "description": $('#ProcessDescription').val(),
        "processtype": $('#ProcessType').val(),
        "rollbacktype": $('#ProcessRollbackType').val()
    };



    var formData = JSON.stringify(data);
    $.ajax({
        type: "POST",
        cache: false,
        data: formData,
        contentType: 'application/json',
        url: ProcessURL,
        success: function(result) {
            alert('Process Added');
            redirectHome();
        },
        error: function(xhr, status, error) {
            alert(status);
            alert(xhr.responseText);
            redirectHome();
        }
    });
}

function setAndOpenProcessModal(processid) {
    $('#UpdProcessHiddenid').val(processid);
    var url = SingleProcessURL.replace("pid", processid);
    $.ajax({
        type: "GET",
        cache: false,
        dataType: 'json',
        contentType: 'application/json',
        url: url,
        success: function(results) {
            var result = results[0];

            $('#UpdProcessName').val(result.processname);
            $('#UpdProcessDescription').val(result.description);
            $('#UpdProcessType').val(result.processtype);
            $('#UpdProcessRollbackType').val(result.rollbacktype);
            $('#UpdateProcessModal').modal('show');
        },
        error: function(xhr, status, error) {
            alert(status);
            alert(xhr.responseText);
            redirectHome();
        }
    });
}

function updateProcess() {
    var processid = $('#UpdProcessHiddenid').val();
    var url = SingleProcessURL.replace("pid", processid);
    var data = {
        "processname": $('#UpdProcessName').val(),
        "description": $('#UpdProcessDescription').val(),
        "processtype": $('#UpdProcessType').val(),
        "rollbacktype": $('#UpdProcessRollbackType').val()

    };

    var formData = JSON.stringify(data);

    $.ajax({
        type: "PUT",
        cache: false,
        data: formData,
        contentType: 'application/json',
        url: url,
        success: function(result) {
            alert('Process Updated');
            redirectHome();
        },
        error: function(xhr, status, error) {
            alert(status);
            alert(xhr.responseText);
            redirectHome();
        }
    });
}

function deleteProcess(processid) {
    var data = {};

    var url = SingleProcessURL.replace("pid", processid);

    var formData = JSON.stringify(data);
    $.ajax({
        type: "DELETE",
        cache: false,
        data: formData,
        contentType: 'application/json',
        url: url,
        success: function(result) {
            alert('Process Deleted');
            redirectHome();
        },
        error: function(xhr, status, error) {
            alert(status);
            alert(xhr.responseText);
            redirectHome();
        }
    });
}

///////////////////////////////////////////////////////////

function addProcessProperty(processid) {
    var url = ProcessPropertyURL.replace("pid", processid);
    var data = {
        "propertyname": $('#ProcessPropertyName').val(),
        "propertytype": $('#ProcessPropertyType').val(),
        "defaultpropertyvalue": $('#ProcessDefaultValue').val()
    };



    var formData = JSON.stringify(data);

    $.ajax({
        type: "POST",
        cache: false,
        data: formData,
        contentType: 'application/json',
        url: url,
        success: function(result) {
            alert('Process Property Added');
            redirectHome();
        },
        error: function(xhr, status, error) {
            alert(status);
            alert(xhr.responseText);
            redirectHome();
        }
    });
}


function setAndOpenProcessPropertyModal(processid, processpropertyid) {
    $('#UpdProcessPropertyHiddenid').val(processpropertyid);

    var url = SingleProcessPropertyURL.replace("pid", processid).replace("ppid", processpropertyid);

    $.ajax({
        type: "GET",
        cache: false,
        dataType: 'json',
        contentType: 'application/json',
        url: url,
        success: function(results) {
            var result = results[0];

            $('#UpdProcessPropertyName').val(result.propertyname);
            $('#UpdProcessPropertyType').val(result.propertytype);
            $('#UpdProcessPropertyDefaultValue').val(result.defaultpropertyvalue);
            $('#UpdateProcessPropertyModal').modal('show');
        },
        error: function(xhr, status, error) {
            alert(status);
            alert(xhr.responseText);
            redirectHome();
        }
    });
}

//        <script>
//    $(document).ready(function(){
//      $('[data-toggle=popover]').popover({
//    content: $('#myPopoverContent').html(),
//    html: true
//}).click(function() {
//    $(this).popover('show');
//})
//    });
//    </script>

function openProcessProperties(processid, processgroupid) {

    var url = ProcessPropertyURL.replace("pid", processid);

    var popover = $('#' + processgroupid);
    //popover.popover();


    $.ajax({
        type: "GET",
        cache: false,
        dataType: 'json',
        contentType: 'application/json',
        url: url,
        success: function(results) {

            $("#records_table tr>td").remove();

            $.each(results, function(i, item) {
                var $tr = $('<tr>').append(
                    $('<td>').text(item.propertyname),
                    $('<td>').text(item.defaultpropertyvalue)
                ).appendTo('#records_table');
            });


            popover.popover('destroy').popover({
                    placement: "right",
                    html: true,
                    content: $('#myPopoverContent').html()
                })
                .popover('show');
        },
        error: function(xhr, status, error) {
            alert(status);
            alert(xhr.responseText);
            redirectHome();
        }
    });


}




function updateProcessProperty(processid) {
    var processpropertyid = $('#UpdProcessPropertyHiddenid').val();
    var url = SingleProcessPropertyURL.replace("pid", processid).replace("ppid", processpropertyid);
    var data = {
        "propertyname": $('#UpdProcessPropertyName').val(),
        "propertytype": $('#UpdProcessPropertyType').val(),
        "defaultpropertyvalue": $('#UpdProcessPropertyDefaultValue').val()
    };

    var formData = JSON.stringify(data);

    $.ajax({
        type: "PUT",
        cache: false,
        data: formData,
        contentType: 'application/json',
        url: url,
        success: function(result) {
            alert('Process Property Updated');
            redirectHome();
        },
        error: function(xhr, status, error) {
            alert(status);
            alert(xhr.responseText);
            redirectHome();
        }
    });
}




function deleteProcessProperty(processid, processpropertyid) {
    var data = {};

    var url = SingleProcessPropertyURL.replace("pid", processid).replace("ppid", processpropertyid);

    var formData = JSON.stringify(data);
    $.ajax({
        type: "DELETE",
        cache: false,
        data: formData,
        contentType: 'application/json',
        url: url,
        success: function(result) {
            alert('Process Property Deleted');
            redirectHome();
        },
        error: function(xhr, status, error) {
            alert(status);
            alert(xhr.responseText);
            redirectHome();
        }
    });
}
///////////////////////////////////////////////////////////

function addLoadPlan() {

    var data = {
        "loadplanname": $('#loadplanname').val(),
        "loadplancategory": $('#loadplancategory').val(),
        "loadplantype": $('#loadplantype').val(),
        "description": $('#loadplandescription').val()
    };



    var formData = JSON.stringify(data);
    $.ajax({
        type: "POST",
        cache: false,
        data: formData,
        contentType: 'application/json',
        url: LoadPlanURL,
        success: function(result) {
            alert('Load Plan Added');
            redirectHome();
        },
        error: function(xhr, status, error) {
            alert(status);
            alert(xhr.responseText);
            redirectHome();
        }
    });
}


function addLoadPlanTemplate() {

    var data = {
        "loadplanname": $('#loadplanname').val(),
        "loadplancategory": $('#loadplancategory').val(),
        "loadplantype": $('#loadplantype').val(),
        "description": $('#loadplandescription').val()
    };



    var formData = JSON.stringify(data);
    $.ajax({
        type: "POST",
        cache: false,
        data: formData,
        contentType: 'application/json',
        url: LoadPlanTemplateURL,
        success: function(result) {
            alert('Load Plan Template Added');
            redirectHome();
        },
        error: function(xhr, status, error) {
            alert(status);
            alert(xhr.responseText);
            redirectHome();
        }
    });
}


function setAndOpenLoadPlanModal(loadplanid) {
    $('#UpdLoadPlanHiddenid').val(loadplanid);

    var url = SingleLoadPlanURL.replace("lpid", loadplanid);

    $.ajax({
        type: "GET",
        cache: false,
        dataType: 'json',
        contentType: 'application/json',
        url: url,
        success: function(results) {
            var result = results[0];

            $('#Updloadplanname').val(result.loadplanname);
            $('#Updloadplancategory').val(result.loadplancategory);
            $('#Updloadplandescription').val(result.description);
            $('#Updloadplantype').val(result.loadplantype);
            $('#UpdateLoadPlanModal').modal('show');
        },
        error: function(xhr, status, error) {
            alert(status);
            alert(xhr.responseText);
            redirectHome();
        }
    });
}

function updateLoadPlan() {
    var loadplanid = $('#UpdLoadPlanHiddenid').val();
    var url = SingleLoadPlanURL.replace("lpid", loadplanid);
    var data = {
        "loadplanname": $('#Updloadplanname').val(),
        "loadplancategory": $('#Updloadplancategory').val(),
        "description": $('#Updloadplandescription').val(),
        "loadplantype": $('#Updloadplantype').val()
    };

    var formData = JSON.stringify(data);

    $.ajax({
        type: "PUT",
        cache: false,
        data: formData,
        contentType: 'application/json',
        url: url,
        success: function(result) {
            alert('Process Property Updated');
            redirectHome();
        },
        error: function(xhr, status, error) {
            alert(status);
            alert(xhr.responseText);
            redirectHome();
        }
    });
}

function deleteLoadPlan(loadplanid) {

    var data = {};
    var url = SingleLoadPlanURL.replace("lpid", loadplanid);
    var formData = JSON.stringify(data);
    $.ajax({
        type: "DELETE",
        cache: false,
        data: formData,
        contentType: 'application/json',
        url: url,
        success: function(result) {
            alert('Load Plan Deleted');
            redirectHome();
        },
        error: function(xhr, status, error) {
            alert(status);
            alert(xhr.responseText);
            redirectHome();
        }
    });
}

///////////////////////////////////////////////////////////


/*function addLoadPlanTemplate() {

      var data = {
                  "loadplanname": $('#loadplanname').val(),
                  "loadplancategory": $('#loadplancategory').val(),
                  "loadplantype": $('#loadplantype').val(),
                  "description": $('#loadplandescription').val()
                };



      var formData = JSON.stringify(data);
      $.ajax({
            type: "POST",cache: false,data: formData,contentType: 'application/json',
            url: LoadPlanTemplateURL,
            success: function(result) {alert('Load Plan Template Added');
            alert(result.loadplanid);
            redirectHome();},
            error: function(xhr, status, error) {alert(status);alert(xhr.responseText);redirectHome();}
            });
      }*/


function setAndOpenLoadPlanTemplateModal(loadplanid) {
    $('#UpdLoadPlanTemplateHiddenid').val(loadplanid);

    var url = SingleLoadPlanTemplateURL.replace("lpid", loadplanid);

    $.ajax({
        type: "GET",
        cache: false,
        dataType: 'json',
        contentType: 'application/json',
        url: url,
        success: function(results) {
            var result = results[0];

            $('#Updloadplantemplatename').val(result.loadplanname);
            $('#Updloadplantemplatecategory').val(result.loadplancategory);
            $('#Updloadplantemplatedescription').val(result.description);
            $('#Updloadplantemplatetype').val(result.loadplantype);
            $('#UpdateLoadPlanTemplateModal').modal('show');
        },
        error: function(xhr, status, error) {
            alert(status);
            alert(xhr.responseText);
            redirectHome();
        }
    });
}

function updateLoadPlanTemplate() {
    var loadplanid = $('#UpdLoadPlanTemplateHiddenid').val();
    var url = SingleLoadPlanTemplateURL.replace("lpid", loadplanid);
    var data = {
        "loadplanname": $('#Updloadplantemplatename').val(),
        "loadplancategory": $('#Updloadplantemplatecategory').val(),
        "description": $('#Updloadplantemplatedescription').val(),
        "loadplantype": $('#Updloadplantemplatetype').val()
    };

    var formData = JSON.stringify(data);

    $.ajax({
        type: "PUT",
        cache: false,
        data: formData,
        contentType: 'application/json',
        url: url,
        success: function(result) { redirectHome(); },
        error: function(xhr, status, error) {
            alert(status);
            alert(xhr.responseText);
            redirectHome();
        }
    });
}

function deleteLoadPlanTemplate(loadplanid) {

    var data = {};
    var url = SingleLoadPlanTemplateURL.replace("lpid", loadplanid);
    var formData = JSON.stringify(data);
    $.ajax({
        type: "DELETE",
        cache: false,
        data: formData,
        contentType: 'application/json',
        url: url,
        success: function(result) {
            alert('Load Plan Template Deleted');
            redirectHome();
        },
        error: function(xhr, status, error) {
            alert(status);
            alert(xhr.responseText);
            redirectHome();
        }
    });
}





///////////////////////////////////////////////////////////
function addProcessGroup(loadplanid) {
    var url = ProcessGroupURL.replace("lpid", loadplanid)
    var data = {
        "processgroupname": $('#ProcessGroupName').val(),
        "processid": $('#ProcessGroupProcessid').val(),
        "orderofexecution": $('#ProcessGroupOrderOfExecution').val(),
        "loadplanid": loadplanid
    };



    var formData = JSON.stringify(data);
    $.ajax({
        type: "POST",
        cache: false,
        data: formData,
        contentType: 'application/json',
        url: url,
        success: function(result) {
            alert('Process Group Added');
            redirectHome();
        },
        error: function(xhr, status, error) {
            alert(status);
            alert(xhr.responseText);
            redirectHome();
        }
    });
}



function setAndOpenProcessGroupModal(loadplanid, processgroupid) {
    $('#UpdProcessGroupHiddenid').val(processgroupid);

    var url = SingleProcessGroupURL.replace("lpid", loadplanid).replace("pgid", processgroupid);

    $.ajax({
        type: "GET",
        cache: false,
        dataType: 'json',
        contentType: 'application/json',
        url: url,
        success: function(results) {
            var result = results[0];

            $('#Updprocessgroupname').val(result.processgroupname);
            $('#Updprocessgrouporderofexecution').val(result.orderofexecution);
            $('#UpdateProcessGroupModal').modal('show');
        },
        error: function(xhr, status, error) {
            alert(status);
            alert(xhr.responseText);
            redirectHome();
        }
    });
}

function updateProcessGroup(loadplanid) {
    var processgroupid = $('#UpdProcessGroupHiddenid').val();
    var url = SingleProcessGroupURL.replace("lpid", loadplanid).replace("pgid", processgroupid);
    var data = {
        "processgroupname": $('#Updprocessgroupname').val(),
        "orderofexecution": $('#Updprocessgrouporderofexecution').val()
    };

    var formData = JSON.stringify(data);

    $.ajax({
        type: "PUT",
        cache: false,
        data: formData,
        contentType: 'application/json',
        url: url,
        success: function(result) {
            alert('Process Group Updated');
            redirectHome();
        },
        error: function(xhr, status, error) {
            alert(status);
            alert(xhr.responseText);
            redirectHome();
        }
    });
}



function deleteProcessGroup(loadplanid, processgroupid) {

    var data = {};
    var url = SingleProcessGroupURL.replace("lpid", loadplanid).replace("pgid", processgroupid);
    var formData = JSON.stringify(data);
    $.ajax({
        type: "DELETE",
        cache: false,
        data: formData,
        contentType: 'application/json',
        url: url,
        success: function(result) {
            alert('Process Group Deleted');
            redirectHome();
        },
        error: function(xhr, status, error) {
            alert(status);
            alert(xhr.responseText);
            redirectHome();
        }
    });
}


///////////////////////////////////////////////////////////

function addProcessGroupTemplate(loadplanid) {
    var url = ProcessGroupTemplateURL.replace("lpid", loadplanid)
    var data = {
        "processgroupname": $('#ProcessGroupName').val(),
        "processid": $('#ProcessGroupProcessid').val(),
        "orderofexecution": $('#ProcessGroupOrderOfExecution').val(),
        "loadplanid": loadplanid
    };



    var formData = JSON.stringify(data);

    $.ajax({
        type: "POST",
        cache: false,
        data: formData,
        contentType: 'application/json',
        url: url,
        success: function(result) {
            alert('Process Group Added');
            redirectHome();
        },
        error: function(xhr, status, error) {
            alert(status);
            alert(xhr.responseText);
            redirectHome();
        }
    });
}



function setAndOpenProcessGroupTemplateModal(loadplanid, processgroupid) {
    $('#UpdProcessGroupHiddenid').val(processgroupid);

    var url = SingleProcessGroupTemplateURL.replace("lpid", loadplanid).replace("pgid", processgroupid);

    $.ajax({
        type: "GET",
        cache: false,
        dataType: 'json',
        contentType: 'application/json',
        url: url,
        success: function(results) {
            var result = results[0];

            $('#Updprocessgroupname').val(result.processgroupname);
            $('#Updprocessgrouporderofexecution').val(result.orderofexecution);
            $('#UpdateProcessGroupModal').modal('show');
        },
        error: function(xhr, status, error) {
            alert(status);
            alert(xhr.responseText);
            redirectHome();
        }
    });
}

function updateProcessGroupTemplate(loadplanid) {
    var processgroupid = $('#UpdProcessGroupHiddenid').val();
    var url = SingleProcessGroupTemplateURL.replace("lpid", loadplanid).replace("pgid", processgroupid);
    var data = {
        "processgroupname": $('#Updprocessgroupname').val(),
        "orderofexecution": $('#Updprocessgrouporderofexecution').val()
    };

    var formData = JSON.stringify(data);

    $.ajax({
        type: "PUT",
        cache: false,
        data: formData,
        contentType: 'application/json',
        url: url,
        success: function(result) {
            alert('Process Group Updated');
            redirectHome();
        },
        error: function(xhr, status, error) {
            alert(status);
            alert(xhr.responseText);
            redirectHome();
        }
    });
}



function deleteProcessGroupTemplate(loadplanid, processgroupid) {

    var data = {};
    var url = SingleProcessGroupTemplateURL.replace("lpid", loadplanid).replace("pgid", processgroupid);
    var formData = JSON.stringify(data);
    $.ajax({
        type: "DELETE",
        cache: false,
        data: formData,
        contentType: 'application/json',
        url: url,
        success: function(result) {
            alert('Process Group Deleted');
            redirectHome();
        },
        error: function(xhr, status, error) {
            alert(status);
            alert(xhr.responseText);
            redirectHome();
        }
    });
}



function createCustomLoadPlan() {


    var loadplanid;

    // Add load plan
    var data = {
        "loadplanname": $('#loadplanname').val(),
        "loadplancategory": $('#loadplancategory').val(),
        "loadplantype": $('#loadplantype').val(),
        "description": $('#loadplandescription').val()
    };

    var formData = JSON.stringify(data);
    $.ajax({
        type: "POST",
        cache: false,
        data: formData,
        contentType: 'application/json',
        url: LoadPlanURL,
        success: function(result) {
            alert('Load Plan Added');

            loadplanid = result.loadplanid;
            redirectHome();
        },
        error: function(xhr, status, error) {
            alert(status);
            alert(xhr.responseText);
            redirectHome();
        },
        complete: function(data) {
            var oTable = document.getElementById('processgrouptable');

            //gets rows of table
            var rowLength = oTable.rows.length;
            //alert(rowLength);

            //loops through rows
            for (i = 1; i < rowLength; i++) {

                //gets cells of current row
                var oCells = oTable.rows.item(i).cells;

                //gets amount of cells of current row
                var cellLength = oCells.length;
                //alert(cellLength);



                var url = ProcessGroupURL.replace("lpid", loadplanid)
                var data = {
                    "processgroupname": oCells.item(1).innerText,
                    "processid": oCells.item(3).innerText,
                    "orderofexecution": oCells.item(0).innerText,
                    "loadplanid": loadplanid
                };

                var formData = JSON.stringify(data);

                $.ajax({
                    type: "POST",
                    cache: false,
                    data: formData,
                    contentType: 'application/json',
                    url: url,
                    success: function(result) {
                        //alert('Process Group Added');
                        redirectHome();
                    },
                    error: function(xhr, status, error) {
                        alert(status);
                        alert(xhr.responseText);
                        redirectHome();
                    }
                });
            }
        }
    });

}


function addConnectionObject() {


    var connectionobjectheaderid;

    var formname;

    if ($('#connection_type').val() == "Oracle") {
        formname = '#oracle_connection';
    } else if ($('#connection_type').val() == "Blob") {
        formname = '#blob_connection';
    } else {
        formname = '#fileserver_connection';
    }

    var fieldValuePairs = $(formname).serializeArray();
    $.each(fieldValuePairs, function(index, fieldValuePair) {
        // alert("Item " + index + " is [" + fieldValuePair.name + "," + fieldValuePair.value + "]");
    });

    var $inputs = $(formname + ' :input');

    // var $inputs = $('#oracle_connection :input');

    /*
        alert($inputs);
        alert($inputs[0].name);
        alert($($inputs[0]).val());

   alert(formname);*/


    // Add connection object
    var data = {
        "connectionname": $($inputs[0]).val(),
        "connectiontype": $('#connection_type').val()
    };

    var formData = JSON.stringify(data);
    $.ajax({
        type: "POST",
        cache: false,
        data: formData,
        contentType: 'application/json',
        url: ConnectionObjectHeaderURL,
        success: function(result) {
            alert('Connection Object Added');
            connectionobjectheaderid = result.connectionobjectheaderid;
            redirectHome();
        },
        error: function(xhr, status, error) {
            alert(status);
            alert(xhr.responseText);
            redirectHome();
        },
        complete: function(data) {

            // not sure if you wanted this, but I thought I'd add it.
            // get an associative array of just the values.
            var connectiondetailurl = ConnectionObjectDetailURL.replace("cname", $($inputs[0]).val());
            var values = {};
            $inputs.each(function() {
                var data = {
                    "connectionobjectheaderid": connectionobjectheaderid,
                    "attribute": this.name,
                    "value": $(this).val()
                };

                var formData = JSON.stringify(data);
                $.ajax({
                    type: "POST",
                    cache: false,
                    data: formData,
                    contentType: 'application/json',
                    url: connectiondetailurl,
                    success: function(result) { //alert('Connection Added');
                    },
                    error: function(xhr, status, error) {
                        alert(status);
                        alert(xhr.responseText);
                        redirectHome();
                    }
                });
            });
            redirectHome();
        }
    });
}


function setAndOpenConnectionObjectDetailModal(connectionobjectheaderid, connectionobjectdetailid) {
    $('#UpdConnectionDetailHiddenid').val(connectionobjectdetailid);

    var url = SingleConnectionObjectDetailURL.replace("cohid", connectionobjectheaderid).replace("codid", connectionobjectdetailid);

    $.ajax({
        type: "GET",
        cache: false,
        dataType: 'json',
        contentType: 'application/json',
        url: url,
        success: function(results) {
            var result = results[0];
            $('#Updconnectiondetailattribute').val(result.attribute);
            $('#Updconnectiondetailvalue').val(result.value);
            $('#UpdateConnectionDetailModal').modal('show');
        },
        error: function(xhr, status, error) {
            alert(status);
            alert(xhr.responseText);
            redirectHome();
        }
    });
}

function updateConnectionObjectDetail(connectionobjectheaderid) {
    var connectionobjectdetailid = $('#UpdConnectionDetailHiddenid').val();
    var url = SingleConnectionObjectDetailURL.replace("cohid", connectionobjectheaderid).replace("codid", connectionobjectdetailid);
    var data = {
        "attribute": $('#Updconnectiondetailattribute').val(),
        "value": $('#Updconnectiondetailvalue').val()
    };

    var formData = JSON.stringify(data);

    $.ajax({
        type: "PUT",
        cache: false,
        data: formData,
        contentType: 'application/json',
        url: url,
        success: function(result) {
            alert('Connection Detail Updated');
            redirectHome();
        },
        error: function(xhr, status, error) {
            alert(status);
            alert(xhr.responseText);
            redirectHome();
        }
    });
}



function deleteProcessGroup(loadplanid, processgroupid) {

    var data = {};
    var url = SingleProcessGroupURL.replace("lpid", loadplanid).replace("pgid", processgroupid);
    var formData = JSON.stringify(data);
    $.ajax({
        type: "DELETE",
        cache: false,
        data: formData,
        contentType: 'application/json',
        url: url,
        success: function(result) {
            alert('Process Group Deleted');
            redirectHome();
        },
        error: function(xhr, status, error) {
            alert(status);
            alert(xhr.responseText);
            redirectHome();
        }
    });
}