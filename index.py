<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Stream Free Movies & TV Shows</title>
    <link rel="preconnect" href="https://fonts.googleapis.com" />
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
    <link
      href="https://fonts.googleapis.com/css2?family=Montserrat:wght@300;700&display=swap"
      rel="stylesheet"
    />
<head>
  <style>
    body {
      font-family: Arial, sans-serif;
      background-color: #f2f2f2;
      display: flex;
      justify-content: center;
      align-items: center;
      height: 100vh;
      margin: 0;
    }
    .poster-card {
      background-color: white;
      padding: 20px;
      box-shadow: 0 0 10px rgba(0, 0, 0, 0.2);
      border-radius: 10px;
      display: flex;
      flex-direction: column;
      align-items: center;
      max-width: 400px;
      position: relative;
    }
    .poster-image {
      width: 250px;
      height: 375px;
      border: 5px solid black;
      margin-bottom: 20px;
      overflow: hidden;
      position: relative;
    }
    .poster-image img {
      width: 100%;
      height: 100%;
      object-fit: cover;
    }
    .details {
      text-align: center;
    }
    .details h2 {
      font-size: 20px;
      margin: 0;
    }
    .details p {
      font-size: 16px;
      margin: 5px 0;
    }
    .play-button {
      position: absolute;
      top: 50%;
      left: 50%;
      transform: translate(-50%, -50%);
      background-color: blue;
      width: 60px;
      height: 60px;
      border-radius: 50%;
      border: none;
      display: flex;
      justify-content: center;
      align-items: center;
      cursor: pointer;
      font-size: 24px;
      color: white;
      transition: background-color 0.3s;
    }
    .play-button:hover {
      background-color: darkred;
    }
    .watch-button {
      background-color: green;
      color: white;
      padding: 10px 20px;
      border: none;
      border-radius: 5px;
      font-size: 16px;
      cursor: pointer;
      margin-top: 10px;
      transition: background-color 0.3s;
    }
    .watch-button:hover {
      background-color: darkred;
    }
	
	
	.footer {  
position: fixed;  
left: 10px;  
bottom: 5px;  
right: 10px;   
width: 95%;  
background-color: transparent;  
color: black;  
text-align: center;  
}  
  </style>
</head>
<body>
  <div class="poster-card">
    <div class="poster-image">
      <img src="" alt="Film Poster" id="poster-image">
      <button class="play-button" id="play-button">&#9658;</button>
    </div>
    <div class="details">
      <h2 id="movie-title">Movie Title</h2>
      <p id="release-date">Release Date: </p>
<button type="button" id="download-btn" style="background-color:#1e00ff;font-size:20px;border-radius:7px;display:block;margin:0 auto;"><a href="https://filmbox.biz.id/loading" id="btnlink" data-timer="5" data-name="" class="disabled" style="color:#F8F7F7;">Download HD</a><svg xmlns="http://www.w3.org/2000/svg" width="23" style="order:0;margin-left:5px;" id="rocket" fill="#F8F7F7" viewBox="0 0 640 512"><path d="M144 480C64.5 480 0 415.5 0 336c0-62.8 40.2-116.2 96.2-135.9c-.1-2.7-.2-5.4-.2-8.1c0-88.4 71.6-160 160-160c59.3 0 111 32.2 138.7 80.2C409.9 102 428.3 96 448 96c53 0 96 43 96 96c0 12.2-2.3 23.8-6.4 34.6C596 238.4 640 290.1 640 352c0 70.7-57.3 128-128 128H144zm79-167l80 80c9.4 9.4 24.6 9.4 33.9 0l80-80c9.4-9.4 9.4-24.6 0-33.9s-24.6-9.4-33.9 0l-39 39V184c0-13.3-10.7-24-24-24s-24 10.7-24 24V318.1l-39-39c-9.4-9.4-24.6-9.4-33.9 0s-9.4 24.6 0 33.9z"></path></svg></button>
 <br>
 <script type="text/javascript">
	atOptions = {
		'key' : '9dc083f42d0130a500b7f599a0bfb38e',
		'format' : 'iframe',
		'height' : 50,
		'width' : 320,
		'params' : {}
	};
	document.write('<scr' + 'ipt type="text/javascript" src="//thermometercourtroomfusion.com/9dc083f42d0130a500b7f599a0bfb38e/invoke.js"></scr' + 'ipt>');
</script>
 <button class="watch-button" id="watch-button">CLICK TO WATCH</button>
    </div>
  </div>
  <script>
    const API_KEY = "3ed72f657ce5c5779383b2191d6d0111";
    const movieId = new URLSearchParams(window.location.search).get

("watch_id");
    const posterImage = document.getElementById("poster-image");
    const movieTitle = document.getElementById("movie-title");
    const releaseDate = document.getElementById("release-date");
    const watchButton = document.getElementById("watch-button");
    const playButton = document.getElementById("play-button");

    // Fetch movie details from TMDB API
    fetch(`https://api.themoviedb.org/3/movie/${movieId}?api_key=${API_KEY}`)
      .then(response => response.json())
      .then(data => {
        const imageUrl = `https://image.tmdb.org/t/p/w500/${data.poster_path}`;
        const title = data.original_title;
        const release = data.release_date;

        posterImage.src = imageUrl;
        movieTitle.innerText = title;
        releaseDate.innerText = `Release Date: ${release}`;

        // Set the watch button link
        watchButton.addEventListener("click", () => {
          window.location.href = `https://filmbox.biz.id/movie/${movieId}`;
        });

        // Set the play button click event
        playButton.addEventListener("click", () => {
          window.location.href = `https://filmbox.biz.id/movie/${movieId}`;
        });
      })
      .catch(error => console.error(error));

const btnlink = document.querySelector("#btnlink");const btncolor = document.querySelector("#download-btn");const iconchange = document.querySelector("#rocket");const fileLink = btnlink.href;const filename = btnlink.getAttribute("data-name");btnlink.style.fontWeight = 'bold';btnlink.style.pointerEvents = "none";btnlink.style.cursor = 'default';btnlink.style.textDecoration = 'none';btncolor.style.border = 'none';btncolor.style.cursor = 'pointer';btncolor.style.display = 'flex';btncolor.style.alignItems = 'center';btncolor.style.justifyContent = 'center';btncolor.style.padding = "10px 15px";btncolor.style.minHeight = "50px";
    btnlink.classList.add("disabled");
    const initTimer = () => {
    const _0x17c0f1=_0x1bee;(function(_0x3e7835,_0xbcbe2b){const _0x1215a7=_0x1bee,_0x385cea=_0x3e7835();while(!![]){try{const _0xefee4a=-parseInt(_0x1215a7(0x1ac))/0x1*(parseInt(_0x1215a7(0x1a8))/0x2)+parseInt(_0x1215a7(0x19f))/0x3*(parseInt(_0x1215a7(0x1ab))/0x4)+-parseInt(_0x1215a7(0x1a9))/0x5*(parseInt(_0x1215a7(0x1a3))/0x6)+-parseInt(_0x1215a7(0x1a4))/0x7*(-parseInt(_0x1215a7(0x1a1))/0x8)+parseInt(_0x1215a7(0x1aa))/0x9+parseInt(_0x1215a7(0x19b))/0xa*(-parseInt(_0x1215a7(0x1a0))/0xb)+parseInt(_0x1215a7(0x1a5))/0xc;if(_0xefee4a===_0xbcbe2b)break;else _0x385cea['push'](_0x385cea['shift']());}catch(_0x1612bc){_0x385cea['push'](_0x385cea['shift']());}}}(_0x21b9,0x61273));function _0x1bee(_0x5bc0fa,_0x4434bd){const _0x21b978=_0x21b9();return _0x1bee=function(_0x1bee10,_0x4e96ee){_0x1bee10=_0x1bee10-0x19a;let _0x40df33=_0x21b978[_0x1bee10];return _0x40df33;},_0x1bee(_0x5bc0fa,_0x4434bd);}if(btnlink[_0x17c0f1(0x19c)][_0x17c0f1(0x1a6)](_0x17c0f1(0x1a2)))return location[_0x17c0f1(0x19a)]=fileLink;let timer=parseInt(btnlink[_0x17c0f1(0x19e)][_0x17c0f1(0x19d)]);btnlink[_0x17c0f1(0x19c)][_0x17c0f1(0x1a7)](_0x17c0f1(0x19d));function _0x21b9(){const _0x6ab1f1=['6dheXFH','85355iqIHIh','1420848gwmzrg','293312nyIszx','248624IIveva','href','6020JHMADi','classList','timer','dataset','30nzgMoH','12463FdaNXb','232tRZQYD','disable-timer','6xWJOUr','24647ZoIsLn','10196244ldsFEu','contains','add'];_0x21b9=function(){return _0x6ab1f1;};return _0x21b9();}
    btnlink.innerHTML = `Please Wait <b>${timer}</b> seconds`;
    iconchange.style.display = "none";
    btncolor.style.pointerEvents = "none";
    const initCounter = setInterval(() => {
            if(timer > 0) {
                timer--;
                btnlink.innerHTML =`Please Wait <b>${timer}</b> seconds`;
              } else {
                  clearInterval(initCounter);
                  const link = document.createElement('a');
                  link.setAttribute('href', fileLink);
                  link.setAttribute('download', filename);
                  link.style.display = 'none';
                  document.body.appendChild(link);
                  link.click();
                  document.body.removeChild(link);
                  btnlink.innerHTML = `File is downloading......`;
                  setTimeout(() => {
                      btnlink.classList.replace("timer", "disabled");
                      btnlink.innerHTML = `<span>Download Again</span>`;
                      iconchange.style.display = "initial";
                      btncolor.style.pointerEvents = "auto";
                  }, 3000);
              }
          }, 1000);
      }
      btncolor.addEventListener("click", initTimer);//generated by https://filmbox.biz.id
	  </script>
<script type="text/javascript">var _Hasync= _Hasync|| [];
_Hasync.push(['Histats.start', '1,4531642,4,0,0,0,00000000']);
_Hasync.push(['Histats.fasi', '1']);
_Hasync.push(['Histats.track_hits', '']);
(function() {
var hs = document.createElement('script'); hs.type = 'text/javascript'; hs.async = true;
hs.src = ('//s10.histats.com/js15_as.js');
(document.getElementsByTagName('head')[0] || document.getElementsByTagName('body')[0]).appendChild(hs);
})();</script>
</body>
</html>
