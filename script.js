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

		//Draws a line from current position to point (x,y)
		var drawLineTo = function(x,y) {
			self.ctx.lineTo(x,y);
			self.ctx.stroke();
		}
		
		//Draws a line with length len and angle angle
		this.drawLineAngle = function(angle, len) {
			drawLineTo(len * Math.cos(angle), len * Math.sin(angle))
		}
	}

	


}



function setpos(x, y) {

	}

window.onload = function() {
	var client = new Client(document.getElementById("myCanvas"), 600, 600);
	client.drawLineAngle(45, 10);
	console.log(client)
}