$( 'button' ).click( function(e) {
    e.preventDefault(); // prevents submitting
    $( 'input' ).trigger( 'click' );
} );