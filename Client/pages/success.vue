<template>
    <section class="my-success">
        <div class="mt-3 row">
            <div class="d-flex flex-column align-items-center">
                <nav aria-label="breadcrumb" class="my-3">
                    <ol class="breadcrumb">
                        <li class="breadcrumb-item">
                            <nuxt-link to="/">Main</nuxt-link>
                        </li>
                        <li class="breadcrumb-item active" aria-current="page">Feedback</li>
                    </ol>
                </nav>
                <!-- feedback sent - logo -->
                <!-- feedback sent - logo -->
                <!-- feedback sent - logo -->
                <div class="text-center lead">
                    <div class="mod">
                        <div class="cube">

                            <div class="faces f1">

                                <div class="dot p1"></div>
                                <div class="dot p2"></div>
                                <div class="dot p3"></div>

                                <div class="dot p4"></div>
                                <div class="dot p5"></div>
                                <div class="dot p6"></div>

                                <div class="dot p7"></div>
                                <div class="dot p8"></div>
                                <div class="dot p9"></div>

                            </div>

                            <div class="faces f2">

                                <div class="dot p10"></div>
                                <div class="dot p11"></div>
                                <div class="dot p12"></div>
                                <div class="dot p13"></div>

                            </div>

                            <div class="faces f3">

                                <div class="dot p1"></div>
                                <div class="dot p2"></div>
                                <div class="dot p3"></div>

                                <div class="dot p4"></div>
                                <div class="dot p5"></div>
                                <div class="dot p6"></div>

                                <div class="dot p7"></div>
                                <div class="dot p8"></div>
                                <div class="dot p9"></div>

                            </div>

                            <div class="faces f4">

                                <div class="dot p10"></div>
                                <div class="dot p11"></div>
                                <div class="dot p12"></div>
                                <div class="dot p13"></div>

                            </div>

                            <div class="faces f5">

                                <div class="dot p1"></div>
                                <div class="dot p2"></div>
                                <div class="dot p3"></div>

                                <div class="dot p4"></div>
                                <div class="dot p5"></div>
                                <div class="dot p6"></div>

                                <div class="dot p7"></div>
                                <div class="dot p8"></div>
                                <div class="dot p9"></div>

                            </div>

                            <div class="faces f6">

                                <div class="dot p10"></div>
                                <div class="dot p11"></div>
                                <div class="dot p12"></div>
                                <div class="dot p13"></div>

                            </div>

                            <div class="faces f7">

                                <div class="dot p1"></div>
                                <div class="dot p2"></div>
                                <div class="dot p3"></div>

                                <div class="dot p4"></div>
                                <div class="dot p5"></div>
                                <div class="dot p6"></div>

                                <div class="dot p7"></div>
                                <div class="dot p8"></div>
                                <div class="dot p9"></div>

                            </div>

                            <div class="faces f8">

                                <div class="dot p10"></div>
                                <div class="dot p11"></div>
                                <div class="dot p12"></div>
                                <div class="dot p13"></div>

                            </div>

                            <div class="faces f9">

                                <div class="dot p1"></div>
                                <div class="dot p2"></div>
                                <div class="dot p3"></div>

                                <div class="dot p4"></div>
                                <div class="dot p5"></div>
                                <div class="dot p6"></div>

                                <div class="dot p7"></div>
                                <div class="dot p8"></div>
                                <div class="dot p9"></div>

                            </div>

                            <div class="faces f10">

                                <div class="dot p10"></div>
                                <div class="dot p11"></div>
                                <div class="dot p12"></div>
                                <div class="dot p13"></div>

                            </div>

                            <div class="faces f11">

                                <div class="dot p1"></div>
                                <div class="dot p2"></div>
                                <div class="dot p3"></div>

                                <div class="dot p4"></div>
                                <div class="dot p5"></div>
                                <div class="dot p6"></div>

                                <div class="dot p7"></div>
                                <div class="dot p8"></div>
                                <div class="dot p9"></div>

                            </div>

                        </div>
                        <div class="project-name">
                            <div class="l1">FEEDBACK SENT</div>
                            <br>
                            <div class="l2">THANK YOU!</div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>
</template>

<script>
export default {
    name: 'Success',
    mounted() {
        try {
            const colorMode = localStorage.getItem("colorMode");
            if (colorMode === null) {
                throw new Error("The color theme switched to light-mode as default");
            } else {
                if (colorMode == "dark") {
                    $(".dot").css("background", "rgb(7, 151, 98)");
                } else {
                    $(".dot").css("background", "#000000");
                }
            }
        } catch (e) {
            $(".dot").css("background", "#000000");
        }
    },
}
</script>