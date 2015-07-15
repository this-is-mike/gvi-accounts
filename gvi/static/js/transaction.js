/**
 * Created by daniel on 30/06/15.
 */
$(document).ready(function() {
    $(window).load(function() {
        lockSelections();
        datepickers();
        datepickersTransactions();
    });
});

function enableDatePicker(){
    datepickersForm();
}

function lockSelections(){
    var lockCategory = function () {
        if ($("#enableCategory").is(":checked")) {
            $('#categorySelect').prop('disabled', false);
        }
        else {
            $('#categorySelect').prop('disabled', 'disabled');
            $('#subcategorySelect').prop('disabled', 'disabled');
        }
    };

    var lockSubcategory = function () {
        if ($("#enableSubcategory").is(":checked")) {
            $('#subcategorySelect').prop('disabled', false);
            $('#enableCategory').prop('checked', true);
            $('#categorySelect').prop('disabled', false);
        }
        else {
            $('#subcategorySelect').prop('disabled', 'disabled');
        }
    };


    $(lockCategory);
    $("#enableCategory").change(lockCategory);
    $("#enableSubcategory").change(lockCategory);
    $(lockSubcategory);
    $("#enableSubcategory").change(lockSubcategory);
    $("#enableCategory").change(lockSubcategory);
}


function datepickers(){
    $('#datetimepickerFrom').datetimepicker({
        viewMode: 'years',
        format: 'YYYY-MM-DD',
        pickTime: false,
        defaultDate: new Date()
    })
        .change(dateChanged)
        .on('changeDate', dateChanged);




    $('#datetimepickerTo').datetimepicker({
        viewMode: 'years',
        format: 'YYYY-MM-DD',
        pickTime: false,
        defaultDate: new Date()
    })
        .change(dateChanged)
        .on('changeDate', dateChanged);


}


function datepickersTransactions() {
    $('.datepickTransaction').datetimepicker({
        viewMode: 'years',
        format: 'YYYY-MM-DD',
        pickTime: false,
        defaultDate: new Date()
    })
        .change(dateChangedNewTransaction)
        .on('changeDate', dateChangedNewTransaction);
}

function dateChanged(ev) {
    var fromDate = $('#fromDate').val();
    var toDate = $('#toDate').val();

    fromDate = fromDate.split("-");
    toDate = toDate.split("-");


    if(fromDate[0] > toDate[0]){
        $('button').prop('disabled', true);
        $("#dateError").show(500);


    }
    else if (fromDate[0] == toDate[0] && fromDate[1] > toDate[1]){
        $('button').prop('disabled', true);
        $("#dateError").show(500);
    }
    else if (fromDate[0] == toDate[0] && fromDate[1] == toDate[1] && fromDate[2] > toDate[2]){
        $('button').prop('disabled', true);
        $("#dateError").show(500);
    }
    else{
        $('button').prop('disabled', false);
        $("#dateError").hide(500);
    }

}

function dateChangedNewTransaction(ev) {
    var fromDate = $('#fromDateNewTransaction').val();
    var toDate = $('#toDateNewTransaction').val();

    fromDate = fromDate.split("-");
    toDate = toDate.split("-");


    if(fromDate[0] > toDate[0]){
        $('#modal_saveDetail').prop('disabled', true);
        $("#dateErrorNewTransaction").show(500);


    }
    else if (fromDate[0] == toDate[0] && fromDate[1] > toDate[1]){
        $('#modal_saveDetail').prop('disabled', true);
        $("#dateErrorNewTransaction").show(500);
    }
    else if (fromDate[0] == toDate[0] && fromDate[1] == toDate[1] && fromDate[2] > toDate[2]){
        $('#modal_saveDetail').prop('disabled', true);
        $("#NewTransaction").show(500);
    }
    else{
        $('#modal_saveDetail').prop('disabled', false);
        $("#dateErrorNewTransaction").hide(500);
    }



}