// A buffer to contain the received pixels.
export var pixels = array(pixelCount*3);
pixels[60] = 0xff;
pixels[61] = 0x00;
pixels[62] = 0xff;

//  Working storage to split out the frame components.
var _r = array(pixelCount), _g = array(pixelCount), _b = array(pixelCount);

// A render function to display the received pixels.
var currentFrame = -1;
export function beforeRender(delta) {
    //  Break apart the frame buffer into its RGB components.
    for(var i = 0; i < pixelCount; i++) {
      _r[i] = pixels[i * 3];
      _g[i] = pixels[i * 3 + 1];
      _b[i] = pixels[i * 3 + 2]
    }
}

export function render(index) {
  rgb(_r[index] / 255, _g[index] / 255, _b[index] / 255);
}