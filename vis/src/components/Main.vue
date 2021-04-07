<template>
    <div class="main">
        <h1>Who is actually getting COVID vaccines in MA?</h1>
        <div class="map-container">
            <Map></Map>
        </div>
    </div>
</template>
<script>
import Map from "@/components/Map";

export default {
    name: "Main",
    components: {Map}
}
</script>