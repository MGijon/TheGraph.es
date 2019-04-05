$('body').scrollspy({
    target: '#navbar-example'
})

$('[data-spy="scroll"]').each(function () {
    var $spy = $(this).scrollspy('refresh')
})

$('[data-spy="scroll"]').on('activate.bs.scrollspy', function () {
    // do something…
})

$('[data-spy="scroll"]').on('activate.bs.scrollspy', function () {
    // do something…
})

$('a[data-toggle="tab"]').on('shown.bs.tab', function (e) {
    e.target // newly activated tab
    e.relatedTarget // previous active tab
})
