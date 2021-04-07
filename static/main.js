
const facebookBtn = document.querySelector(".facebook-btn");
const twitterBtn = document.querySelector(".twitter-btn");
const linkedinBtn = document.querySelector(".linkedin-btn");
const whatsappBtn = document.querySelector(".whatsapp-btn");


function get_link(hrefUrl) {
    const spliting = hrefUrl.split("/")
    console.log(hrefUrl)
    youtube_url = "https://www.youtube.com/watch?v=" + spliting[spliting.length-2]
    return youtube_url
}



function init() {
    let postUrl = encodeURI(document.location.href);
    let postTitle = encodeURI("Hi everyone, please check this out: ");
    url= get_link(postUrl)

    facebookBtn.setAttribute(
        "href",
        `https://www.facebook.com/sharer.php?u=${url}`
    );

    twitterBtn.setAttribute(
        "href",
        `https://twitter.com/share?url=${url}&text=${postTitle}`
    );


    linkedinBtn.setAttribute(
        "href",
        `https://www.linkedin.com/shareArticle?url=${url}&title=${postTitle}`
    );

    whatsappBtn.setAttribute(
        "href",
        `https://wa.me/?text=${postTitle} ${url}`
    );
}

init();

