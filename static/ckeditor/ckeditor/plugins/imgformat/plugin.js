/**
 * Copyright (c) 2014-2016, CKSource - Frederico Knabben. All rights reserved.
 * Licensed under the terms of the MIT License (see LICENSE.md).
 *
 * Basic sample plugin inserting current date and time into the CKEditor editing area.
 *
 * Created out of the CKEditor Plugin SDK:
 * http://docs.ckeditor.com/#!/guide/plugin_sdk_intro
 */

// Register the plugin within the editor.
CKEDITOR.plugins.add( 'imgformat', {

	// Register the icons. They must match command names.
	icons: 'imgformat',

	// The plugin initialization logic goes inside this method.
	init: function( editor ) {

		// Define the editor command that inserts a timestamp.
		editor.addCommand( 'insertImgformat', {

			// Define the function that will be fired when the command is executed.
			exec: function( editor ) {

				var selected = editor.getSelection().getSelectedElement();
				selected.removeAttributes();
				selected.removeStyle("width");
				selected.removeStyle("height");
				selected.addClass("image");

				editor.insertHtml(  '<figure class="image-container">');
				editor.insertElement(selected);
				editor.insertHtml('<figcaption class="caption"> caption goes here </figcaption></figure>');
			}
		});

		// Create the toolbar button that executes the above command.
		editor.ui.addButton( 'Imgformat', {
			label: 'Insert Image Format',
			command: 'insertImgformat',
			toolbar: 'plugins'
		});
	}
});
