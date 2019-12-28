$(document).ready(
	function()
	{
		$("#text").text("click here to be flooded with goobledeygook");
		$("#text").click(
			function()
			{
				$("#text").append(" nice day ");
				$("#text").click();
			}
		);
		$("p:not(#text)").click(
			function()
			{
				this.append("clicked");
			}
		)
	}
);
