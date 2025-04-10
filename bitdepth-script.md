What does it actually mean when we say that a video is 8-bit or 10-bit?

Every digital image is made up of pixels. Each pixel has three color channels: Red, Green and Blue.

Giving us a grid like this.

But why these specific numbers? Why is it 76 for RED and not some other number.

You probably know that computers only can store either ones or zeros. That's it. These are the building blocks for all the information we store.

They are called bits and can either be zero or one.

So how do these bits represent color? Let's start simple:

If we had a 1 bit image we can only have 2 different shades of color, 0 and 1. Basically a black and white image.

If we have a 2-bit image our range of colors doubles to 4 or values between 0 and 3.

So each additional bit doubles the amount of color information we store.

Finally we end up at eight bits, giving us 256 unique color values.

The reason 8-bits became standard is becayse computers process information in chunks of 8 bits, called bytes. This byte-based processing made 8-bit color depth a natural choice for early digital systems.

It also gives enough range to make the images look good to our eyes.

Now, let's talk about 10-bit color. We're just adding two more bits to our 8-bit system.

That's a 25% increase in storage size because we go from 8 to 10 bits.

But here's the interesting part: those two extra bits don't just add a few more values. They actually quadruple our color precision, taking us from 256 possible values to 1024.

Think about that: we get 4 times the color fidelity but just increase our storage size by 25%.

However, even at 8-bit a video stream gets very large.

A single HD frame at 8-bit color depth takes up about 6 megabytes of storage.

At 24 frames per second in a video stream, that's 149 megabytes per second. Convert that to bits, and we're looking at over 1200 megabits per second.

So actually what most would consider a very basic HD video at just 8 bit will actually be impossible to stream over a normal internet connection uncompressed.

This leads us to why we need codecs and compression. Lets look at how we can compress color with chroma subsampling such as 422 next.

Let's take a look at human vision. We're much more sensitive to luminance - the brightness information - than we are to color.

Think about a portrait. The luminance differences in her face - between dark eyebrows and lighter skin, between the eyes and the mouth - these differences are what help us read facial expressions and understand the story in an image.

On the other hand, the subtle color variations, like different shades of blue in the sky, don't carry the same importance for our perception of the scene.

This leads to the conclusion that we can compress color much more aggressivley than luminance.

But here's the problem with RGB: luminance and color information are completely intertwined. So how can we reduce color resolution while preserving luminance details? How can we compress one without affecting the other?

This is where YCbCr comes in. You might have also heard of YUV, which is the older standard that uses the same principle.

YCbCr breaks down an image into three components:

- A luma channel (Y), which is essentially the black and white version of the image
- A blue difference channel (Cb)
- A red difference channel (Cr)

Interestingly, this separation has historical roots in television. When color TV was introduced, the same signal could be sent to both old black-and-white tvs and new color TVs. The older ones would just display the luma channel and ignore the color.

So how do we convert from RGB to YCbCr? It's done through this mathematical formula.

Where we first calulate the luma value from our RGB values. But we are actually using different weigts for each channel. We take 70% percent of green, 20% of red and just 2% of blue.

Why is that? Look at these three dots on screen - all are at the same intensity, but the green one appears brightest, red in the middle, and blue the darkest.

This reflects how our eyes work: we're most sensitive to green, then red, and least sensitive to blue. Because of this, the Rec.709 standard have choosen these percentage to align with human visual perception.

And where is the green channel you might ask? We actually dont need to store it since we can just reverse this formula and get it from the luma, blue and red channels.

Now we get this grid of pixels where each pixel has a separate luma and color values.

First up here is 4:4:4 - full resolution - every pixel has its own luma and color information, just like RGB.

To compress the color is now very straight forward. We just throw away part of the color information.

This brings us to 4:2:2 - every pixel still has its own luma value Y, but for every second pixel, we remove the color information.

4:2:0 takes it even further - we both throw away every second pixels color and also every second line of pixels in the image we throw away all color.

You might look at these subsampling patterns and think the image quality would be terrible.

But the fascinating part is that most of the media you consume every day is actually in 4:2:0 format, and it looks fine to our eyes.

While the color information is very imporant in the post production of the image, for the final viewing experience we can compress quite aggressively.

If we overlay 422 and 420 over the original 444 image, the difference is pretty subtle, even when multiplied 10 times.
