

// Register the plugin within the editor.
CKEDITOR.plugins.add( 'wrap', {
	// This plugin requires the Widgets System defined in the 'widget' plugin.
	requires: 'widget',

	// Register the icon used for the toolbar button. It must be the same
	// as the name of the widget.
	icons: 'simplebox',

	// The plugin initialization logic goes inside this method.
	init: function( editor ) {
		// Register the simplebox widget.
		editor.widgets.add( 'wrap', {
			// Allow all HTML elements and classes that this widget requires.
			// Read more about the Advanced Content Filter here:
			// * http://docs.ckeditor.com/#!/guide/dev_advanced_content_filter
			// * http://docs.ckeditor.com/#!/guide/plugin_sdk_integration_with_acf
			allowedContent: 'figure(!image-container); img(!image); figcaption(!caption)',

			// Minimum HTML which is required by this widget to work.
			// requiredContent: 'img(image)'

			// Define two nested editable areas.
			editables: {
				container: {
					// Define a CSS selector used for finding the element inside the widget element.
					selector: '.image-container',
					// Define content allowed in this nested editable. Its content will be
					// filtered accordingly and the toolbar will be adjusted when this editable
					// is focused.
					allowedContent: 'figure'
				},
				image: {
					selector: '.image',
					allowedContent: 'img'
				},
				capiton: {
					selector: '.caption',
					allowedContent: 'figcaption'
				}

			},

			// Define the template of a new Simple Box widget.
			// The template will be used when creating new instances of the Simple Box widget.
			template:
				'<figure class="image-container">' +
					'<image class="image" src="http://placehold.it/100x100">' +
					'<figcaption class="caption"> caption goes here </figcaption>' +
				'</figure>',

			// Define the label for a widget toolbar button which will be automatically
			// created by the Widgets System. This button will insert a new widget instance
			// created from the template defined above, or will edit selected widget
			// (see second part of this tutorial to learn about editing widgets).
			//
			// Note: In order to be able to translate your widget you should use the
			// editor.lang.simplebox.* property. A string was used directly here to simplify this tutorial.
			button: 'Create an image template',

			// Check the elements that need to be converted to widgets.
			//
			// Note: The "element" argument is an instance of http://docs.ckeditor.com/#!/api/CKEDITOR.htmlParser.element
			// so it is not a real DOM element yet. This is caused by the fact that upcasting is performed
			// during data processing which is done on DOM represented by JavaScript objects.
			upcast: function( element ) {
				// Return "true" (that element needs to converted to a Simple Box widget)
				// for all <div> elements with a "simplebox" class.
				return element.name == 'image';
			}
		} );
	}
} );
