/* Project specific Javascript goes here. */

/*
Formatting hack to get around crispy-forms unfortunate hardcoding
in helpers.FormHelper:

    if template_pack == 'bootstrap4':
        grid_colum_matcher = re.compile('\w*col-(xs|sm|md|lg|xl)-\d+\w*')
        using_grid_layout = (grid_colum_matcher.match(self.label_class) or
                             grid_colum_matcher.match(self.field_class))
        if using_grid_layout:
            items['using_grid_layout'] = True

Issues with the above approach:

1. Fragile: Assumes Bootstrap 4's API doesn't change (it does)
2. Unforgiving: Doesn't allow for any variation in template design
3. Really Unforgiving: No way to override this behavior
4. Undocumented: No mention in the documentation, or it's too hard for me to find
*/
$('.form-group').removeClass('row');

// angular.module('tabsDemoDynamicHeight', ['ngMaterial']);

$(function(){
	$("#id_dob").datepicker(
	{
		dateFormat:'yy-mm-dd'
	}
	);
});

$('.ui.radio.checkbox')
  .checkbox()
;
$('select.dropdown')
  .dropdown()
;
$("#id_city").addClass("ui search dropdown");
$("#id_country").addClass("ui search dropdown");
$("#id_body_type").addClass("ui search dropdown");
$("#id_complexion").addClass("ui search dropdown");
$("#id_mother_tonge").addClass("ui search dropdown");



$('#progressbar1').progress({
  percent: 15
});
$('#progressbar2').progress({
  percent: 30
});
$('#progressbar3').progress({
  percent: 45
});

$('#progressbar4').progress({
  percent: 60
});
$('#progressbar5').progress({
  percent: 75
});
$('#progressbar6').progress({
  percent: 100
});

