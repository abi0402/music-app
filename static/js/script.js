var audio = {
    init: function () {
        var $that = this;
        $(function () {
            $that.components.media();  // Corrected function call to 'media'
        });
    },
    components: {
        media: function (target) {  // Corrected function name to 'media'
            var media = $('audio.fc-media', (target !== undefined) ? target : 'body');
            if (media.length) {
                media.mediaelementplayer({
                    audioHeight: 40,
                    features: ['playpause', 'current', 'duration', 'progress', 'volume', 'tracks', 'fullscreen'],
                    alwaysShowControls: true,
                    timeAndDurationSeparator: '<span></span>',
                    iPadUseNativeControls: true,  // Corrected typo in property name
                    iPhoneUseNativeControls: true,  // Corrected typo in property name
                    AndroidUseNativeControls: true  // Corrected typo in property name
                });
            }
        }
    }
}

audio.init();
