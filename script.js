document.addEventListener('DOMContentLoaded', function() {
    const tooltips = document.querySelectorAll('.tooltip');
    tooltips.forEach(tooltip => {
        tooltip.addEventListener('mouseover', showTooltip);
        tooltip.addEventListener('mouseout', hideTooltip);
    });

    function showTooltip(event) {
        const tooltipText = event.currentTarget.getAttribute('data-tooltip');
        // Additional logic to display tooltip can be implemented here
    }

    function hideTooltip(event) {
        // Logic to hide the tooltip
    }
});
