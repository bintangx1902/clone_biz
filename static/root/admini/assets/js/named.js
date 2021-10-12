let x, y, z, vid;
x = document.getElementById('cont');
y = x.getElementsByTagName('img');
vid = x.getElementsByTagName('iframe');
for (z = 0; z < y.length; z++) {
    y[z].className = 'img-fluid';
    y[z].style = null;
    vid[z].style = null;
}

let a, b, c;
a = x.getElementsByTagName('p');
for (c = 0; c < a.length; c++){
    a[c].className = 'text-break';
}

if('{{post.stats}}' === 'DISABLED') {

}

