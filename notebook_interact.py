from IPython.display import HTML
from IPython.display import display, Javascript

def createImage():
    # Create canvas
    display(HTML('<div class="centerclass"><canvas id="sketch" width="200" height="200" /></div>'))
    
    # Create buttons and sketcher object
    source = """
    <script src="src/js/jquery-1.7.min.js"></script>
    <script src="src/js/modernizr.custom.34982.js"></script>

    <script src="src/js/sketcher.js"></script>
    <script src="src/js/trigonometry.js"></script>

    <link rel="stylesheet" href="src/assets/styles.css" />

    <script>
    var sketcher = null;

    $(document).ready(function(e) {
        sketcher = new Sketcher( "sketch" );
    });

    function sendToIPython() {
        var var_name = "sketcher_image";
        var command = var_name + " = '" + sketcher.toString() + "'";
        console.log("Executing Command: " + command);

        var kernel = IPython.notebook.kernel;
        kernel.execute(command);
    }
    </script>

    <button onclick="sketcher.clear();">Clear</button>
    <button onclick="sendToIPython();">Send to IPyton</button>
    """
    display(HTML(source))

def saveImage(image, filename):
    fh = open(filename, "wb")
    fh.write(image.decode('base64'))
    fh.close()
