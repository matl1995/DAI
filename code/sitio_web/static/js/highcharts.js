$(function () { 
    var lista = [];
    $.get('/restaurantes/getgrafico/',
        {},
        function (data) {
            //Genero las tarjetas con los restaurantes
            $('#contenedor-resultado-restaurantes-interior').empty();

            tamanio=data.length;

            for(i=0;i<tamanio;i++)
            {
                var elemento = [];
                elemento.push(data[i].cuisine);
                elemento.push(parseInt(data[i].count));
                lista.push(elemento);
            }

            var myChart = Highcharts.chart('grafico', {
                chart: {
                    type: 'column'
                },
                title: {
                    text: 'Tipos de cocina por cantidad:'
                },
                subtitle: {
                    text: ''
                },
                xAxis: {
                    type: 'category',
                    labels: {
                        rotation: -45,
                        style: {
                            fontSize: '13px',
                            fontFamily: 'Verdana, sans-serif'
                        }
                    }
                },
                yAxis: {
                    min: 0,
                    title: {
                        text: 'Cantidad'
                    }
                },
                legend: {
                    enabled: false
                },
                tooltip: {
                    pointFormat: ''
                },
                series: [{
                    name: 'Tipo cocina',
                    data: lista,
                    dataLabels: {
                        enabled: true,
                        rotation: -90,
                        color: '#FFFFFF',
                        align: 'right',
                        y: 10, // 10 pixels down from the top
                        style: {
                            fontSize: '13px',
                            fontFamily: 'Verdana, sans-serif'
                        }
                    }
                }]
            });
        }
    );
});