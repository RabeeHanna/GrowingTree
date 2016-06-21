class Client {
	constructor(c,x,y) {
		this.canvas = c;
		this.max_height = x;
		this.max_width = y;
		this.x = 0;
		this.y = 0;
		this.ctx = this.CANVAS.getContext("2d");
		this.ctx.moveTo(this.x, this.y);
	}

	drawLineTo(x,y):
}


function setpos(x, y)
	{
		ctx.moveTo(x,y);
		pos = [x,y];
	}

var c = document.getElementById("myCanvas");
var HEIGHT = 600;
var WIDTH = 600;
var pos = [0,0];
c.setAttribute("width", HEIGHT);
c.setAttribute("height", WIDTH);
var ctx = c.getContext("2d");
setpos(round(width/2),HEIGHT);
ctx.lineTo(0,0);
ctx.stroke();