/**
 * Copyright (c) 2003-2015, CKSource - Frederico Knabben. All rights reserved.
 * For licensing, see LICENSE.md or http://ckeditor.com/license
 */

// This file contains style definitions that can be used by CKEditor plugins.
//
// The most common use for it is the "stylescombo" plugin, which shows a combo
// in the editor toolbar, containing all styles. Other plugins instead, like
// the div plugin, use a subset of the styles on their feature.
//
// If you don't have plugins that depend on this file, you can simply ignore it.
// Otherwise it is strongly recommended to customize this file to match your
// website requirements and design properly.

CKEDITOR.stylesSet.add( 'default', [


	/* Inline Styles */


	{ name: 'Title',
	  element: 'h3',
	  attributes:
	  {
	  	'class' : 'Go-Big'
	  }
	},

	{ name: 'Image Caption',
	  element: 'figcaption',
	  attributes:
	  {
  		'class': 'caption'
	  }
	},

	{ name: 'Figure',
	 element: 'figure',
	 attributes:
	 {
	 	'class' : 'image-container'
	 }
	},


] );

