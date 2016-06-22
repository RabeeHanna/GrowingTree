class Client {
	constructor(c,x,y) {
		/*PRIVATE*/
		self = this;
		/*PUBLIC*/
		this.canvas = c;
		this.ctx = c.getContext("2d");
		c.setAttribute("width", x);
		c.setAttribute("height", y);
		this.max_width = x;
		this.max_height = y;
		this.x = 0;
		this.y = 0;
		this.ctx.beginPath();
		this.setpos = function(x,y) {
			this.ctx.moveTo(x,y);
			this.x = x;
			this.y = y;
		}
		this.setpos(x/2, y);
		//this.setpos(200,300);

		//Draws a line from current position to point (x,y) 
		var drawLineTo = function(x,y) {
			self.ctx.lineTo(x,y);
			self.x = x;
			self.y = y;
		}

		this.drawLineAngle = function(angle, len) {
			drawLineTo(len*Math.cos(-angle) + this.x,len*Math.sin(-angle) + this.y);
		}

		//Add the drawing to the canvas
		this.update = function() {
			this.ctx.stroke();
		}
	}
}

var PIOVER180 = (Math.PI / 180);

function toRadians(angle) {
	return angle * PIOVER180;
}

function setpos(x, y) {

	}

window.onload = function() {
	var client = new Client(document.getElementById("myCanvas"), 600, 600);
	client.drawLineAngle(toRadians(45), 50);
	client.drawLineAngle(toRadians(80), 50);
	client.update();
	console.log(client)
}