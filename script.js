class Client {
	constructor(c,x,y) {
		self = this;
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

		var drawLineTo = function(x,y) {
			self.ctx.lineTo(x,y);
			self.x = x;
			self.y = y;
		}

		// Draws a line with a length of 'len' and angle 'angle' and stays at that position
		this.draw = function(angle, len) {
			drawLineTo(len*Math.cos(-angle) + this.x,len*Math.sin(-angle) + this.y);
		}

		// Draws a line with a length of 'len' and angle 'angle' and returns to first position
		this.drawReturn = function(angle, len) {
			var xy = [this.x, this.y]
			drawLineTo(len*Math.cos(-angle) + this.x,len*Math.sin(-angle) + this.y);
			this.setpos(xy[0], xy[1]);
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
	client.draw(toRadians(45), 50);
	client.draw(toRadians(80), 50);
	client.drawReturn(toRadians(40), 30);
	client.drawReturn(toRadians(60), 30);
	client.update();
	console.log(client)
}