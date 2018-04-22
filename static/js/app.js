
// Helpful snippet from http://stackoverflow.com/questions/680241/resetting-a-multi-stage-form-with-jquery
function resetForm($form) {
    $form.find('input:text, input:password, input:file, select, textarea').val('');
    $form.find('input:radio, input:checkbox')
         .removeAttr('checked').removeAttr('selected');
}

// Main App
$(document).ready(function() {

    // Account - Use AJAX to get the Account Edit form and
    // display it on the page w/out a refresh
    $('#gi-container').delegate('.edit-account', 'click', function(e) {
        e.preventDefault();
        $('#gi-container').load($(this).attr('href'));
    });


    // Contact - Use AJAX to get the Contact Add form
    $('#cd-container').delegate('#new-contact', 'click', function(e) {
        e.preventDefault();
        $.get($(this).attr('href'), function(data) {
            $('#cd-body').append(data);
            $('#new-contact').hide();
        });
    });

    // Contact - Use AJAX to get the Contact Edit form
    $('#cd-container').delegate('.edit-contact', 'click', function(e) {
        e.preventDefault();
        var that = $(this);
        $.get($(this).attr('href'), function(data) {
            $('#new-contact').hide();
            that.parent().parent().remove();
            $('#cd-body').append(data);
        })
    });

    // Contact - Use AJAX to save the Contact Add Form
    $('#cd-container').delegate('#contact-form', 'submit', function(e) {
        e.preventDefault();
        var form = $('#contact-form');
        var url = form.attr('action');
        $.post(url, form.serialize(), function(data) {
            if ($(data).find('.errorlist').html()) {
                // If the contact form is returned we know there are errors
                $('#new-contact').hide();
                $('#cd-body').append(data);
            } else {
                // Otherwise insert the row into the table
                $('#cd-table tr:last').after(data);
                $('#new-contact').show();
            }
        });
        $(this).remove(); // Remove the form
    });
});
