var $ = django.jQuery;
$(document).ready(function(){
    $('#id_object_id').parent().append('<div id="lookup_box"></div>');
    $('#id_content_type').change(function () {
        var $selected = $('#id_content_type option:selected')
        var type = $selected.text();
        var pk = $selected.val();
        if (pk === '') {
            $('#lookup_box').html('Select content type first...');
        } else {
            $.get(
                get_ctype_url + '?pk=' + pk,
                function(data) {
                    $('#lookup_box').html('<a id="lookup_id_object_id" class="related-lookup" onclick="return showRelatedObjectLookupPopup(this);"></a>');
                    $('#lookup_id_object_id').html('<img src="'+ static_url + 'admin/img/selector-search.gif"/> Lookup ' + type);
                    $('#lookup_id_object_id').attr('href', admin_url + data.app_label +'/'+ data.model +'/?t=id');
                }
            )
        }
    }).change();
});
