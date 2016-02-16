$(document).ready(function() {
    var app = {}

    app.init = function() {

        console.log("Controles inicializados..");
        app.clickController();
    }

    app.clickController = function() {
        $token = $("#token").val();
        $user = $("#user").val();

        $(".controle").on("click", function() {
            $command = $(this).data('command');
            app.sendCommand($command, $token, 1);
        });
    }

    app.sendCommand = function(command, token, user) {
        $.ajax({
            url: '/api/robot/command/' + user + '/',
            type: 'PUT',
            data: {
                'command': command
            },
            headers: {
                'Authorization':  'Token ' + token 
            },
            success: function(data) {
                console.log('comando salvo com sucesso..');
            },
            error: function(data) {
                alert("Algum erro está acontecendo com o envio do comando..");
            }

        });
    }

    app.init();
})