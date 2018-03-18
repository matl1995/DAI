function paginador(b,t,n,max) {
    $.get('/restaurantes/getpagina/',
        {pagina:n, busqueda:b, tipo:t},
        function (data) {
            //Genero las tarjetas con los restaurantes
            $('#contenedor-resultado-restaurantes-interior').empty();

            tamanio=data.length;

            for(i=0;i<tamanio;i++)
            {
                $('#contenedor-resultado-restaurantes-interior').append(`<div class="col-auto" id="columna-tarjetas">
                        <div class="card">
                            <div class="card-body">
                                <h4 class="card-title">`+data[i].name+`</h4>
                                <h6 class="card-subtitle mb-2 text-muted">Tipo: `+data[i].cuisine+`</h6>
                                <p class="card-text">Barrio: `+data[i].borough+`</p>
                            </div>
                        </div>
                    </div>`);
            }

            //Genero el nuevo paginador
            $('#paginador').empty();
            if(n==0)
            {
                $('#paginador').append(`<ul class="pagination justify-content-center">
                    <li class="page-item" style="pointer-events:none;opacity:0.7;"><a class="page-link" href="#" onclick="paginador('`+b+`','`+t+`',0,`+max+`);">Previous</a></li>
                    <li class="page-item"><a class="page-link" href="#" onclick="paginador('`+b+`','`+t+`',0,`+max+`);">0</a></li>
                    <li class="page-item"><a class="page-link" href="#" onclick="paginador('`+b+`','`+t+`',1,`+max+`);">1</a></li>
                    <li class="page-item"><a class="page-link" href="#" onclick="paginador('`+b+`','`+t+`',1,`+max+`);">Next</a></li>
                </ul>`);
            }
            else if(n==max-1)
            {
                $('#paginador').append(`<ul class="pagination justify-content-center">
                    <li class="page-item"><a class="page-link" href="#" onclick="paginador('`+b+`','`+t+`',`+(n-1)+`,`+max+`);">Previous</a></li>
                    <li class="page-item""><a class="page-link" href="#" onclick="paginador('`+b+`','`+t+`',`+(n-1)+`,`+max+`);" >`+(n-1)+`</a></li>
                    <li class="page-item"><a class="page-link" href="#" onclick="paginador('`+b+`','`+t+`',`+n+`,`+max+`);">`+n+`</a></li>
                    <li class="page-item" style="pointer-events:none;opacity:0.7;"><a class="page-link" href="#" onclick="paginador('`+b+`','`+t+`',`+n+`,`+max+`);">Next</a></li>
                </ul>`);
            }
            else
            {
                $('#paginador').append(`<ul class="pagination justify-content-center">
                    <li class="page-item"><a class="page-link" href="#" onclick="paginador('`+b+`','`+t+`',`+(n-1)+`,`+max+`);">Previous</a></li>
                    <li class="page-item""><a class="page-link" href="#" onclick="paginador('`+b+`','`+t+`',`+(n-1)+`,`+max+`);" >`+(n-1)+`</a></li>
                    <li class="page-item"><a class="page-link" href="#" onclick="paginador('`+b+`','`+t+`',`+n+`,`+max+`);">`+n+`</a></li>
                    <li class="page-item"><a class="page-link" href="#" onclick="paginador('`+b+`','`+t+`',`+(n+1)+`,`+max+`);">`+(n+1)+`</a></li>
                    <li class="page-item"><a class="page-link" href="#" onclick="paginador('`+b+`','`+t+`',`+(n+1)+`,`+max+`);">Next</a></li>
                </ul>`);
            }
        }
    );
};