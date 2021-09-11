function readFile(src, tgt) {

    var fileToRead = document.getElementById(src);

    var fReader = new FileReader();
    fReader.readAsText(fileToRead.files[0]);
    fReader.onload = (function(e) {

        var content = document.getElementById(tgt);
        content.value = e.target.result;
    })

}

function writeFile(content, tgtFileName) {

    blob = new Blob([content], {type: "octet/stream"});
    var a = document.createElement("a");
    url = window.URL.createObjectURL(blob);
    a.href = url;
    a.download = tgtFileName;
    a.click();
    window.URL.revokeObjectURL(url);
}

function ImportArtefact() {
     var data = $('#ArtefactImportFileContent').val();

    $.ajax({
        type: "POST",
        cache: false,
        data: data,
        contentType: 'application/json',
        url: SingleArtefactImportURL,
        success: function(result) {
            alert(JSON.stringify(result));

            redirectHome();
        },
        error: function(xhr, status, error) {
            alert(status);
            alert(xhr.responseText);
            redirectHome();
        }
    });



}

function DownloadDDLSQL(artefactid) {
    var url = SingleArtefactDDLURL.replace("aid", artefactid);
    $.ajax({
        type: "GET",
        cache: false,
        dataType: 'json',
        contentType: 'application/json',
        url: url,
        success: function(results) {
            var fileName =   artefactid + ".sql"
            writeFile(results, fileName)
        },
        error: function(xhr, status, error) {
            alert(status);
            alert(xhr.responseText);
            redirectHome();
        }
    });
}

function ExportArtefact(artefactid) {
    var url = SingleArtefactExportURL.replace("aid", artefactid);
    $.ajax({
        type: "GET",
        cache: false,
        dataType: 'json',
        contentType: 'application/json',
        url: url,
        success: function(results) {
            var content = JSON.stringify(results,null,2);
            var fileName =   artefactid + ".json"
            writeFile(content, fileName)
        },
        error: function(xhr, status, error) {
            alert(status);
            alert(xhr.responseText);
            redirectHome();
        }
    });
}

function addArtefact() {


    var data = {
        "artefactname": $('#Aartefactname').val(),
        "loadplanid": $('#Aloadplanid').val(),
        "artefacttype": $('#Aartefacttype').val(),
        'executionfrequencyid': $('#AddArtefactExecutionFrequency').val(),
        'executionCron': $('#AddArtefactExecutionCron').val(),
        'executionfrequencymanager': $('#AddArtefactExecutionFrequencyMgmt').val(),
        "category": $('#Acategory').val(),
        "description": $('#Adescription').val(),
        "businessdescription": $('#Abusinessdescription').val(),

        "columnlistcontent": $('#ArtefactColumnListFileContent').val()
    };



    var formData = JSON.stringify(data);

    $.ajax({
        type: "POST",
        cache: false,
        data: formData,
        contentType: 'application/json',
        url: ArtefactURL,
        success: function(result) {
            alert(JSON.stringify(result));
            alert(result.Msg);
            redirectHome();
        },
        error: function(xhr, status, error) {
            alert(status);
            alert(xhr.responseText);
            redirectHome();
        }
    });
}


function setAndOpenArtefactModal(artefactid) {
    $('#UpdateArtefactHiddenid').val(artefactid);
    var url = SingleArtefactURL.replace("aid", artefactid);
    $.ajax({
        type: "GET",
        cache: false,
        dataType: 'json',
        contentType: 'application/json',
        url: url,
        success: function(results) {
            var result = results[0];

            $("#UpdateArtefactName").val(result.artefactname);
            $("#UpdateArtefactType").val(result.artefacttype);
            $("#UpdateArtefactCategory").val(result.category);
            $('#UpdateArtefactDescription').val(result.description);
            $('#UpdateArtefactBusinessDescription').val(result.businessdescription);
            $('#UpdateArtefactExecutionFrequency').val(result.executionfrequency);
            $('#UpdateArtefactExecutionManager').val(result.executionfrequencymanager);

            $('#UpdateArtefactModal').modal('show');
        },
        error: function(xhr, status, error) {
            alert(status);
            alert(xhr.responseText);
            redirectHome();
        }
    });
}




function updateArtefact() {
    var artefactid = $('#UpdateArtefactHiddenid').val();
    var url = SingleArtefactURL.replace("aid", artefactid);
    var data = {
        "artefactname": $("#UpdateArtefactName").val(),
        "artefacttype": $("#UpdateArtefactType").val(),
        "category": $("#UpdateArtefactCategory").val(),
        "description": $('#UpdateArtefactDescription').val(),
        "businessdescription": $('#UpdateArtefactBusinessDescription').val(),
        "executionfrequency": $('#UpdateArtefactExecutionFrequency').val(),
        "executionfrequencymanager": $('#UpdateArtefactExecutionManager').val()
    };

    var formData = JSON.stringify(data);

    $.ajax({
        type: "PUT",
        cache: false,
        data: formData,
        contentType: 'application/json',
        url: url,
        success: function(result) {
            alert('Artefact Updated');
            redirectHome();
        },
        error: function(xhr, status, error) {
            alert(status);
            alert(xhr.responseText);
            redirectHome();
        }
    });
}

function deleteArtefact(artefactid) {


    var data = {};

    var url = SingleArtefactURL.replace("aid", artefactid);

    var formData = JSON.stringify(data);
    $.ajax({
        type: "DELETE",
        cache: false,
        data: formData,
        contentType: 'application/json',
        url: url,
        success: function(result) {
            alert('Artefact Deleted');
            redirectHome();
        },
        error: function(xhr, status, error) {
            alert(status);
            alert(xhr.responseText);
            redirectHome();
        }
    });
}

function deployonTAC(artefactid) {

    var data = {};

    var url = SingleArtefactURL.replace("aid", artefactid);

    var formData = JSON.stringify(data);
    $.ajax({
        type: "POST",
        cache: false,
        data: formData,
        contentType: 'application/json',
        url: url,
        success: function(result) {
            alert('Artefact Deployed on TAC');
            redirectHome();
        },
        error: function(xhr, status, error) {
            alert(status);
            alert(xhr.responseText);
            redirectHome();
        }
    });

}

/////////////////////////////////////////////////////

function addArtefactProperty(artefactid) {

    var url = ArtefactPropertyURL.replace("aid", artefactid);
    var data = {
        "propertyname": $('#ArtefactPropertyName').val(),
        "description": $('#ArtefactPropertyDescription').val(),
        "propertyvalue": $('#ArtefactPropertyValue').val()
    };



    var formData = JSON.stringify(data);

    $.ajax({
        type: "POST",
        cache: false,
        data: formData,
        contentType: 'application/json',
        url: url,
        success: function(result) {
            alert('Artefact Property Added');
            redirectHome();
        },
        error: function(xhr, status, error) {
            alert(status);
            alert(xhr.responseText);
            redirectHome();
        }
    });
}

function setAndOpenArtefactPropertyModal(artefactid, artefactpropertyid) {
    $('#UpdateArtefactPropertyHiddenid').val(artefactpropertyid);
    var url = SingleArtefacPropertytURL.replace("aid", artefactid).replace("apid", artefactpropertyid);
    $.ajax({
        type: "GET",
        cache: false,
        dataType: 'json',
        contentType: 'application/json',
        url: url,
        success: function(results) {
            var result = results[0];
            $("#UpdateArtefactPropertypropertyname").val(result.propertyname);
            $("#UpdateArtefactdescription").val(result.description);
            $("#UpdateArtefactpropertyvalue").val(result.propertyvalue);

            $('#UpdateArtefactPropertyModal').modal('show');
        },
        error: function(xhr, status, error) {
            alert(status);
            alert(xhr.responseText);
            redirectHome();
        }
    });
}




function updateArtefactProperty(artefactid) {
    var artefactpropertyid = $('#UpdateArtefactPropertyHiddenid').val();
    var url = SingleArtefacPropertytURL.replace("aid", artefactid).replace("apid", artefactpropertyid);
    var data = {
        "propertyname": $("#UpdateArtefactPropertypropertyname").val(),
        "description": $("#UpdateArtefactdescription").val(),
        "propertyvalue": $("#UpdateArtefactpropertyvalue").val()
    };

    var formData = JSON.stringify(data);

    $.ajax({
        type: "PUT",
        cache: false,
        data: formData,
        contentType: 'application/json',
        url: url,
        success: function(result) {
            alert('Artefact Property Updated');
            redirectHome();
        },
        error: function(xhr, status, error) {
            alert(status);
            alert(xhr.responseText);
            redirectHome();
        }
    });
}

function deleteArtefactProperty(artefactid, artefactpropertyid) {

    var data = {};

    var url = SingleArtefacPropertytURL.replace("aid", artefactid).replace("apid", artefactpropertyid);
    alert(url);
    var formData = JSON.stringify(data);
    $.ajax({
        type: "DELETE",
        cache: false,
        data: formData,
        contentType: 'application/json',
        url: url,
        success: function(result) {
            alert('Artefact Property Deleted');
            redirectHome();
        },
        error: function(xhr, status, error) {
            alert(status);
            alert(xhr.responseText);
            redirectHome();
        }
    });
}

/////////////////////////////////////////////////////

function setAndOpenArtefactProcessPropertyModal(artefactid, artefactprocesspropertyid, processpropertyid, processgroupid, processid, propertyname, propertyvalue) {

    if (artefactprocesspropertyid == '') {
        $('#CreateArtefactProcessPropertyHiddenName').val(propertyname);
        $("#CreateArtefactprocesspropertyvalue").val(propertyvalue);
        $("#CreateArtefactprocesspropertyid").val(processpropertyid);
        $("#CreateAPPprocessgroupid").val(processgroupid);
        $("#CreateAPPprocessid").val(processid);
        $('#CreateArtefactProcessPropertyModal').modal('show');
    } else {
        $('#UpdateArtefactProcessPropertyHiddenid').val(artefactprocesspropertyid);
        var url = SingleArtefacProcessPropertytURL.replace("aid", artefactid).replace("appid", artefactprocesspropertyid);
        $.ajax({
            type: "GET",
            cache: false,
            dataType: 'json',
            contentType: 'application/json',
            url: url,
            success: function(results) {
                var result = results[0];
                $("#UpdateArtefactprocesspropertyvalue").val(result.propertyvalue);

                $('#UpdateArtefactProcessPropertyModal').modal('show');
            },
            error: function(xhr, status, error) {
                alert(status);
                alert(xhr.responseText);
                redirectHome();
            }
        });
    }
}


function addArtefactProcessProperty(artefactid) {
    var url = ArtefactProcessPropertyURL.replace("aid", artefactid);
    var data = {
        "propertyvalue": $("#CreateArtefactprocesspropertyvalue").val(),
        "processpropertyid": $("#CreateArtefactprocesspropertyid").val(),
        "processgroupid": $("#CreateAPPprocessgroupid").val(),
        "processid": $("#CreateAPPprocessid").val()
    };

    var formData = JSON.stringify(data);

    $.ajax({
        type: "POST",
        cache: false,
        data: formData,
        contentType: 'application/json',
        url: url,
        success: function(result) {
            alert('Artefact Process Property Updated');
            redirectHome();
        },
        error: function(xhr, status, error) {
            alert(status);
            alert(xhr.responseText);
            redirectHome();
        }
    });


}


function updateArtefactProcessProperty(artefactid) {
    var artefactprocesspropertyid = $('#UpdateArtefactProcessPropertyHiddenid').val();
    var url = SingleArtefacProcessPropertytURL.replace("aid", artefactid).replace("appid", artefactprocesspropertyid);
    var data = {
        "propertyvalue": $("#UpdateArtefactprocesspropertyvalue").val()
    };

    var formData = JSON.stringify(data);

    $.ajax({
        type: "PUT",
        cache: false,
        data: formData,
        contentType: 'application/json',
        url: url,
        success: function(result) {
            alert('Artefact Process Property Updated');
            redirectHome();
        },
        error: function(xhr, status, error) {
            alert(status);
            alert(xhr.responseText);
            redirectHome();
        }
    });
}


/////////////////////////////////////////////////////

function addArtefactDependency(artefactid) {

    var url = ArtefactDependencyURL.replace("aid", artefactid);
    var data = {
        "parentartefactid": $('#AddArtefactParentDependnecy').val()
    };

    var formData = JSON.stringify(data);

    $.ajax({
        type: "POST",
        cache: false,
        data: formData,
        contentType: 'application/json',
        url: url,
        success: function(result) {
            alert('Artefact Dependency Added');
            redirectHome();
        },
        error: function(xhr, status, error) {
            alert(status);
            alert(xhr.responseText);
            redirectHome();
        }
    });
}


function deleteArtefactDependency(artefactid, artefactdependencyid) {
    var data = {};
    var url = SingleArtefactDependencyURL.replace("aid", artefactid).replace("adid", artefactdependencyid);
    var formData = JSON.stringify(data);
    $.ajax({
        type: "DELETE",
        cache: false,
        data: formData,
        contentType: 'application/json',
        url: url,
        success: function(result) {
            alert('Artefact Dependency Deleted');
            redirectHome();
        },
        error: function(xhr, status, error) {
            alert(status);
            alert(xhr.responseText);
            redirectHome();
        }
    });
}

//////////////////////////////////////////////////////

function addArtefactExecutionInterval(artefactid) {

    var url = ArtefactExecutionIntervalURL.replace("aid", artefactid);
    var data = {
        "executionfrequencyid": $('#AddArtefactExecutionFrequency').val()
    };

    var formData = JSON.stringify(data);

    $.ajax({
        type: "POST",
        cache: false,
        data: formData,
        contentType: 'application/json',
        url: url,
        success: function(result) {
            alert('Artefact Execution Interval Added');
            redirectHome();
        },
        error: function(xhr, status, error) {
            alert(status);
            alert(xhr.responseText);
            redirectHome();
        }
    });
}


/////////////////////////////////////////////////////
function addArtefactAttribute(artefactid) {


    var url = ArtefactAttributeURL.replace("aid", artefactid)
    var data = {
        "isidentifier": $("#artefactattributeisidentifier").val(),
        "isnullable": $('#artefactattributeisnullable').val(),
        "technicalname": $('#artefactattributetechnicalname').val(),
        "businessname": $('#artefactattributebusinessname').val(),
        "datatype": $('#artefactattributedatatypeid').val(),
        "ordinalposition": $('#artefactattributeordinalposition').val(),
        "precision": $('#artefactattributeprecision').val(),
        "scale": $('#artefactattributescale').val(),
        "maxlength": $('#artefactattributemaxlength').val()
    };

    var formData = JSON.stringify(data);
    $.ajax({
        type: "POST",
        cache: false,
        data: formData,
        contentType: 'application/json',
        url: url,
        success: function(result) {
            alert('Artefact Attribute Added');
            redirectHome();
        },
        error: function(xhr, status, error) {
            alert(status);
            alert(xhr.responseText);
            redirectHome();
        }
    });

}



function setAndOpenArtefactAttributeModal(artefactid, artefactattributeid) {
    $('#UpdateArtefactAttributeHiddenid').val(artefactattributeid);
    var url = SingleArtefactAttributeURLtURL.replace("aid", artefactid).replace("attid", artefactattributeid);
    $.ajax({
        type: "GET",
        cache: false,
        dataType: 'json',
        contentType: 'application/json',
        url: url,
        success: function(results) {
            var result = results[0];

            $("#updateartefactattributeisidentifier").val(result.isidentifier);
            $('#updateartefactattributeisnullable').val(result.isnullable);
            $('#updateartefactattributetechnicalname').val(result.technicalname);
            $('#updateartefactattributebusinessname').val(result.businessname);
            $('#updateartefactattributeordinalposition').val(result.ordinalposition);
            $('#updateartefactattributeprecision').val(result.precision);
            $('#updateartefactattributescale').val(result.scale);
            $('#updateartefactattributemaxlength').val(result.maxlength);
            $('#updateartefactattributedatatypeid').val(result.datatype)

            $('#UpdateArtefactAttributeModal').modal('show');
        },
        error: function(xhr, status, error) {
            alert(status);
            alert(xhr.responseText);
            redirectHome();
        }
    });
}




function updateArtefactAttribute(artefactid) {
    var artefactattributeid = $('#UpdateArtefactAttributeHiddenid').val();
    var url = SingleArtefactAttributeURLtURL.replace("aid", artefactid).replace("attid", artefactattributeid);
    var data = {
        "isidentifier": $("#updateartefactattributeisidentifier").val(),
        "isnullable": $('#updateartefactattributeisnullable').val(),
        "technicalname": $('#updateartefactattributetechnicalname').val(),
        "businessname": $('#updateartefactattributebusinessname').val(),
        "datatype": $('#updateartefactattributedatatypeid').val(),
        "ordinalposition": $('#updateartefactattributeordinalposition').val(),
        "precision": $('#updateartefactattributeprecision').val(),
        "scale": $('#updateartefactattributescale').val(),
        "maxlength": $('#updateartefactattributemaxlength').val()
    };

    var formData = JSON.stringify(data);

    $.ajax({
        type: "PUT",
        cache: false,
        data: formData,
        contentType: 'application/json',
        url: url,
        success: function(result) {
            alert('Artefact Attribute Updated');
            redirectHome();
        },
        error: function(xhr, status, error) {
            alert(status);
            alert(xhr.responseText);
            redirectHome();
        }
    });
}

function deleteArteAttribute(artefactid, artefactattributeid) {

    var data = {};
    var url = SingleArtefactAttributeURLtURL.replace("aid", artefactid).replace("attid", artefactattributeid);
    var formData = JSON.stringify(data);
    $.ajax({
        type: "DELETE",
        cache: false,
        data: formData,
        contentType: 'application/json',
        url: url,
        success: function(result) {
            alert('Artefact Attribute Deleted');
            redirectHome();
        },
        error: function(xhr, status, error) {
            alert(status);
            alert(xhr.responseText);
            redirectHome();
        }
    });
}