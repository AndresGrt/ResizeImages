const Jimp = require('jimp')
const path = require('path')

const resizeIMG = async (images, width, quiality) => {
    const image = await Jimp.read(images[0])
    await image.resize(width, Jimp.AUTO)
            .quality(quiality)
            .writeAsync(images[1])
}

const arryResize = (value, configID) => {
    console.log('START value = ', value)
    return new Promise(() => {
        value.forEach(async element => {
            const options = {
                images: [path.join(__dirname, `../public/StreamingAssets/${configID}/uploads_high/${element}`),path.join(__dirname, `../public/StreamingAssets/${configID}/uploads/${element}`)],
                width:512,
                quality:45
            }
            await resizeIMG(options.images, options.width, options.quality)
        });
    })
}

module.exports = { resizeIMG, arryResize }
