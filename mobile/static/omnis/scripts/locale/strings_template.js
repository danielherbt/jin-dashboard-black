/**
 LOCALIZATION STRINGS

 This file is provided as a human readable version of string_base.js as a template for creating localized strings.

 The default strings (in member 'base') are used when there is no value for the current locale, so it is recommended that
 you do not remove strings_base.js from your locale folder.

 Other locales can be plugged in as members (all lowercase), and should be contained in it's own strings file
 e.g. "en_us" in "strings_en_us.js, "fr" in "strings_fr.js".

 The HTML file which points to your Omnis library should have a <script> line containing an array of supported languages,
 which should look like:
 		<script>var supportedLanguages = ["fr","de","it","en_us"];</script>
 Note: base is not specified in this list as it is loaded automatically.
 The Omnis JS Client will automatically detect the locale of the client and load the relevant locale strings (if they
 are specified in supportedLanguages)

 The client will search for strings in the full locale (e.g. en_us), then the language locale (e.g. en), then base.
 An exception will be thrown if the string cannot be found in any of the above.

 \x01 place-holders are used to parameterize the text, and their value is described in the relevant comment
 */
jOmnisStrings.base = // The member of jOmnisStrings is the locale code (e.g. french would be jOmnisStrings.fr)
{
	// ** OBJECT MEMBER **									** STRING **

	// COMPONENT SPECIFIC STRINGS
	// Calendar/Date/Time Picker
		ctl_date_calendar_button:							"Open date picker", // alt-text for calendar button in a popup datepicker
		ctl_date_time_button:									"Open time picker", // alt-text for time button in a popup timepicker
		ctrl_date_increase:										"Increase", // aria-label for increase button
		ctrl_date_decrease:										"Decrease", // aria-label for decrease button
		ctrl_date_header:											["Select a Month", "Select a Year", "Select a Decade", "Select a Time"], // text for date picker header ("Select a Time" is not currently used)

		// Charts (Bar/Pie)
		ctl_piechart_segment:									"\x01 of \x01", // text for screen reader when navigating through segments of a pie chart (params: current segment number, total number of segments)
		ctl_barchart_bar:											"\x01 of \x01", // text for screen reader when navigating through bars of a bars chart (params: current bar number, total number of bar)

		// Data grid
		ctl_dgrd_id:													"You cannot use \x01 as a list column name for a list bound to a data grid", // Error text for using an invalid list column name in a datagrid (param: column name)
		ctl_dgrd_others:											"(\x01 others)", // Info text describing number of other rows, shown when dragging rows (param: number of other rows)
		ctl_dgrd_other:												"(1 other)", // Info text describing 1 other row, shown when dragging rows
		ctl_dgrd_filter:											"Filter", // aria-label for filter button
		ctl_dgrd_bool_checked:								"Checked", // aria-label for checked boolean input
		ctl_dgrd_bool_notchecked:							"Not checked", // aria-label for not-checked boolean input
		ctl_dgrd_color_input:									"Color value", // aria-label for color input
		ctl_dgrd_color_input_desc:						"Acceptable formats: hex, rgb, or color name", // description for color input used in an aria-describedby element
		ctl_dgrd_filter_none:         				"No Filter:?", // Data grid filter: No filter description
		ctl_dgrd_filter_equals:       				"Equals:==", // Data grid filter: Equals filter description
		ctl_dgrd_filter_notequals:    				"Not Equals:!==", // Data grid filter: Not equals filter description
		ctl_dgrd_filter_contains:     				"Contains:=", // Data grid filter: Contains filter description
		ctl_dgrd_filter_notcontains:  				"Not Contains:!=", // Data grid filter: Not contains filter description
		ctl_dgrd_filter_lessthan:     				"Less Than:<", // Data grid filter: Less than filter description
		ctl_dgrd_filter_morethan:     				"More Than:>", // Data grid filter: More than filter description
		ctl_dgrd_filter_lessthanequal:				"Less Than or Equal:<=", // Data grid filter: Less than or equal to filter description
		ctl_dgrd_filter_morethanequal:				"More Than or Equal:>=", // Data grid filter: More than or equal to filter description
		ctl_dgrd_filter_empty:        				"Empty:??", // Data grid filter: Empty filter description
		ctl_dgrd_filter_notempty:     				"Not Empty:!??", // Data grid filter: Not empty filter description

		// Dialogs and Subform Sets
		omn_dialog_close:											"Close dialog", // close button text
		omn_subform_close:										"Close \x01 dialog", // close button text on a subform within a subform set (param: title of subform)
		omn_subform_closepanel:								"Close \x01 panel", // close button text on a subform panel within a subform set (param: title of panel)
		omn_subform_min:											"Minimise \x01 dialog", // minimize button text on a subform within a subform set (param: title of subform)
		omn_subform_max:											"Maximise \x01 dialog", // maximize button text on a subform within a subform set (param: title of subform)
		omn_subform_restore:									"Restore \x01 dialog", // restore button text on a subform within a subform set (param: title of subform)
		omn_subform_collapse:									"Collapse \x01 panel", // collapse button text on a subform panel within a subform set (param: title of subform)
		omn_subform_expand:										"Expand \x01 panel", // expand button text on a subform panel within a subform set (param: title of subform)
		omn_subform_paneltitle:								"\x01. \x01 of \x01", // aria-label text for a subform within a subform set (params: title of subform, subform number within this set, total number of subforms)
		omn_subform_dialogtitle:							"\x01. \x01 of \x01", // aria-label text for a subform panel within a subform set (params: title of panel, panel number within this set, total number of panels)
		omn_inst_badformlist:									"\x01: Invalid formlist", // Invalid form list error text (param: Omnis instance)
		omn_inst_badparent:										"\x01: Invalid parent for subform set", // Invalid parent for subform set error text (param: Omnis instance)
		omn_inst_badpn:												"\x01: Paged pane does not have page \x01", // Paged pane does not have the given page for subform set error text (params: Omnis instance, page number)
		omn_inst_badpp:												"\x01: Cannot find the paged pane with name \"\x01\"", // Paged pane does not exist error text (params: Omnis instance, paged pane name)
		omn_inst_badsfsname:									"\x01: Invalid or empty name for subform set", // Subform set name is invalid or empty error text (param: Omnis instance)
		omn_inst_dupsfsname:									"\x01: A subform set named \"\x01\" already exists", // Subform set name already exists error text (param: command name, subform set name)
		omn_inst_dupuid:											"Subform set already contains unique id \x01", // Subform set already contains unique id error text (param: id)
		omn_inst_sfsnotthere:									"\x01: A subform set with name \"\x01\" does not exist", // Subform set does not exists error text (params: Omnis instance, subform set name)

		// Droplist
		ctl_drop_button:											"Show options", // droplist/combo arrow button aria-label

		// File
		ctl_file_batchsizeerror:							"Total batch of files is larger than maximum allowed upload size (\x01)", // Error text for exceeding maximum upload size of a batch of files (param: $maxbatchuploadsize)
		ctl_file_filesizeerror:								"File size is larger than maximum allowed upload size (\x01)// \x01 //", // Error text for exceeding maximum upload size of a single file (params: $maxfileuploadsize, list of files)
		ctl_file_downloaderror:								"Download error", // Error text for a download error
		ctl_file_uploadtitle:									"Upload file", // Dialog title to upload a file
		ctl_file_uploadmultipletitle: 				"Upload files", // Dialog title to upload multiple files
		ctl_file_uploadbutton:								"Upload", // Upload button text
		ctl_file_stopbutton:									"Cancel upload", // Cancel upload button text
		ctl_file_filesizetext:								"\x01 of \x01", // Upload file size text (params: current progress size, total file size)
		ctl_file_batchsizetext:								"\x01 of \x01", // Upload batch size text (params: current progress size, total batch size)
		ctl_file_filesuploaded:								"\x01/\x01 files", // Number of files uploaded (params: number of files uploaded, total number of files to upload)
		ctl_file_uploaderror:									"Upload error", // Upload error text
		ctl_file_uploadstopped:								"Upload stopped", // Upload stopped text
		ctl_file_closedialog:									"Close file upload dialog", // aria-label text for file dialog close button
		ctl_file_choosefile:									"Choose file", // aria-label text for choose file button
		ctl_file_choosefiles:									"Choose files", // aria-label text for choose files button
		ctl_file_selected:										"\x01 files selected", // Label text showing how many files selected (param: number of files currently selected)

		// Map
		ctl_map_defaultlabel:									"Map", // Map control aria-label

		// Native Switch
		switch_on:														"ON", // Switch on text
		switch_off:														"OFF", // Switch off text

		// Pager
		omn_pager_previous:										"Previous page", // aria-label text for previous button
		omn_pager_next:												"Next page", // aria-label text for next button
		omn_pager_page:												"Page", // aria-label text for current page

		// Split Button
		ctl_splitbutton_openmenu:							"Open menu", // aria-label text for split button open menu

		// Subform
		ctl_subf_params:											"Control \x01: $parameters cannot be assigned at runtime", // Error message text when $parameters has been assigned at runtime (param: subform control name)

		// Tab
		ctl_tabs_scrollleft:									"Scroll left", // Tabs arrow button aria-label left text
		ctl_tabs_scrollright:									"Scroll right", // Tabs arrow button aria-label right text
		ctl_tabs_scrollup:										"Scroll up", // Tabs arrow button aria-label up text
		ctl_tabs_scrolldown:									"Scroll down", // Tabs arrow button aria-label down text

		// Toolbar
		ctl_toolbar_sidemenu:									"Side menu", // aria-label for hamburger button
		ctl_toolbar_overflowmenu:							"Overflow menu", // aria-label for overflow button
		ctl_toolbar_selected_item:						"\x01 selected",	// aria-label for selected item elements

		// Tree
		ctl_tree_invmode:											"Control \x01: Invalid data mode for tree", // Error text for invalid data mode for tree control (param: control name)
		ctl_tree_badident:										"Control \x01: You cannot use \x01 as a tree node ident - tree node idents must be a non-zero positive integer", // Error text for a node ident (params: control name, ident number)
		ctl_tree_dupident:										"Control \x01: The tree already has a node with ident \x01 - tree node idents must be unique", // Error text for duplicate node ident (params: control name, ident number)
		ctl_tree_badgnl:											"Control \x01: Internal error calling get node line for dynamic tree", // Error text for node line error in a dynamic tree (param: control name)
		ctl_tree_expand:											"Expand node", // aria-label for expand node button
		ctl_tree_collapse:										"Collapse node", // aria-label for collapse node button

		// OMNIS/JSCLIENT STRINGS
		// General
		error:																"Error", // Generic error text
		local_storage_unavailable_error:			"Unable to access localStorage (perhaps cookies are disabled?).//The application will not run.", // Local storage unavailable error text
		comms_timeout:												"The server has not responded.  Press OK to continue waiting", // Server comms timeout error text
		comms_error:													"An error has occurred when communicating with the server.  Press OK to retry the request", // Server comms error text
		disconnected:													"You have been disconnected. Refresh or restart application to reconnect", // Disconnected error text
		// Generic date/time strings
		month_names:													["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"], // Full month names
		month_names_short:										["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"], // Abbreviated month names
		day_names:														["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"], // Full day names
		day_names_short:											["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"], // Abbreviated day names
		date_units:														["Day", "Month", "Year", "Decade"], // Date units
		time_units:														["Hour", "Minute", "Second", "Millisecond"], // Time units

		// Text escape errors
		omnis_badhtmlesc:											"Invalid HTML escape", // Invalid HTML escape error text
		omnis_badstyleesc:										"Invalid style escape sequence", // Invalid style escape sequence error text
		omnis_escnotsupp:											"Text escape not supported by JavaScript client", // Text escape not supported error text
		// Data conversion errors
		omnis_convbad:												"Error setting \x01: variable type \x01 not supported by JavaScript client", // Error setting variable text (params: variable name, variable type)
		omnis_convbool:												"Error setting \x01: data cannot be converted to Boolean", // Error setting Boolean text (param: variable name)
		omnis_convchar:												"Error setting \x01: data cannot be converted to Character", // Error setting Character text (param: variable name)
		omnis_convdate:												"Error setting \x01: data cannot be converted to Date", // Error setting Date text (param: variable name)
		omnis_convint:												"Error setting \x01: data cannot be converted to Integer", // Error setting Integer text (param: variable name)
		omnis_convnum:												"Error setting \x01: data cannot be converted to Number", // Error setting Number text (param: variable name)
		omnis_convlist:												"Error setting \x01: data cannot be converted to List", // Error setting List text (param: variable name)
		omnis_convrow:												"Error setting \x01: data cannot be converted to Row", // Error setting Row text (param: variable name)
		// Form errors
		omn_form_ctrlinst:										"Failed to install the control \x01. Possible missing class script", // Failed to install control text (param: control name)
		omn_form_addsrc:											"Cannot find source object \x01 for add control", // Cannot find source object error text (param: source obj name)
		omn_form_addparent:										"Cannot find parent object \x01 for add control", // Cannot find parent object error text (param: parent obj name)
		omn_form_addbadparent:								"Parent object \"\x01\" for add control is not a paged pane", // Parent object is not a paged pane error text (param: parent obj name)
		omn_form_addbadpage:									"Parent page number \x01 not valid for paged pane \"\x01\"", // Parent page number error text (params: page number, paged pane name)
		omn_form_addcg:												"Cannot add control to parent object \x01 contained in complex grid", // Cannot add control to parent contained in complex grid error text (param: parent obj name)
		omn_form_nofile:											"There is no file with the specified ident (\x01)", // No file with given ident error (param: file ident)
		omn_form_readfileerror:								"Error \x01 occurred when reading the file with ident \x01", // Error message when reading file (params: error name, file ident)
		omn_form_noinstvar:										"Instance variable does not exist (\x01)", // Instance variable does not exist error (param: variable name)
		// Instance errors
		omn_inst_badservmethcall:							"Cannot make server method call when waiting for a response from the server", // Cannot call server method when waiting for a response error text
		omn_inst_cliexcep:										"Exception occurred when executing client method://", // Exception when executing client method error text
		omn_inst_excep:												"Exception occurred when processing server response://", // Exception when processing server response error text
		omn_inst_excepfile:										"File \"\x01\" Line \x01//", // Exception in file error text (params: file name, line number)
		omn_inst_formnum:											"Invalid form number. Parameter error \x01", // Invalid form number (param: error)
		omn_inst_objnum:											"Invalid object number. Parameter error \x01", // Invalid object number (param: error)
		omn_inst_respbad:											"Unknown response received from server", // Unknown response from server error text
		omn_inst_xmlhttp:											"Failed to initialize XMLHttpRequest", // Could not initialize XMLHttpRequest error text
		omn_inst_assignpdf:										"Assign PDF: HTML control \"\x01\" not found", // HTML control not found when assigning PDF error text (param: HTML control name)

		// Client errors
		omn_cli_callprivate:									"callprivate cannot call \"\x01\"://Exception: \x01", // Cannot call private method error text (params: method name, error)
		omn_cli_badobj:												"object $objs.\x01 does not exist", // Object does not exist error text (param: object name)
		omn_cli_cgcanassign:									"cannot use $canassign for row section object \"\x01\" in complex grid because it has exceptions", // Cannot use $canassign on an object in the row section of a complex grid when the complex grid has exceptions error text (param: object name)
		omn_cli_openpush:											"Unable to open Push Connection.//(\x01)", // Unable to open a Push Connection (param: Attempted push connection URL)

		// Lists
		omn_list_badaddcols:									"The argument count for $addcols must be a multiple of 4", // $addcols must be a multiple of 4 error text
		omn_list_badrow:											"Invalid list row", // Invalid row error text

		// Client language settings
		omn_cli_locale_change_title:					"Client Locale Changed", // Dialog title when client locale is changed via clientcommand "setlocale" or "clearlocale"
		omn_cli_locale_change_msg:						"The change in locale settings will not take effect until the application is reloaded.//Would you like to reload now?////Note: Any unsaved changes will be lost!" // Dialog message when client locale is changed via clientcommand "setlocale" or "clearlocale"
};