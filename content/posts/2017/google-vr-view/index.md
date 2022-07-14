---
title: 'Google VR View'
date: '2017-01-23'
tags: ['VR', 'google']
draft: false
summary: 'You can embed 360° photos and videos into a website using VR View. This looks great on both desktop and smartphone. On mobile devices even the movement is registered and integrated. When you turn your smartphone, the image or video also rotates.'
---

You can embed 360° photos and videos into a website using VR View. This looks great on both desktop and smartphone. On mobile devices even the movement is registered and integrated. When you turn your smartphone, the image or video also rotates.

### Sample from Google

Google provides web developers with a free sample on [Github](https://github.com/googlevr/vrview) of how to integrate VR View into your own site.

First you have to integrate the VR View script into your page. Either you link it directly from Google or you put a copy of it on your own server.

```html
<script src="//storage.googleapis.com/vrview/2.0/build/vrview.min.js"></script>
```

Next, create a "div" element with the class "vrview" on your page:

```html
<div id="vrview"></div>
```

Finally, a little Javascript is missing:  

```javascript
window.addEventListener('load', onVrViewLoad)
function onVrViewLoad() {
  var vrView = new VRView.Player('#vrview', {
    video: 'link/to/video.mp4',
    is_stereo: true
  });
}
```

This displays a VR View element on its own page.  

### How to integrate VR View into Neos

I wrote for you a Neos CMS plugin. This plugin provides you a NodeType available, where you can easily define your own photos or videos. The NodeType takes these media and creates a VR View element from it.  
  
All you have to do is simply load [my package](https://github.com/gerdemann/Gerdemann.VRView) via [Composer](https://getcomposer.org/) into your site:  

```bash
composer require "gerdemann/vrview:~1.0"
```

### Features

My plugin has the following features:

* You can use your own image or video
* You can set the width and height of the element
* You can define whether it is a stereo medium
* And you can define the starting angle

### How to create 360° images or videos

Just use one of the many [360 ° cameras](https://www.amazon.de/gp/search/ref=as_li_qf_sp_sr_tl?ie=UTF8&camp=1638&creative=6742&index=aps&keywords=360%20Kamera&linkCode=ur2&tag=wsn08-21) (affiliate link) or alternatively use Google's StreetView app for [iPhone](https://itunes.apple.com/de/app/google-street-view/id904418768?mt=8) or [Android](https://play.google.com/store/apps/details?id=com.google.android.street&hl=de).  

### Conclusion

Let yourself be inspired by this simple plugin to write also an extension for the great CMS Neos! :-)