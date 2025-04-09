from manim import *
import random

config.frame_width = 16
config.frame_height = 9

# RENDER ALL
# manim -pgh bit-depth.py BinaryToColor RGBPixelGrid BitDepthExplanation RGBCircles ValueRangeComparison StorageCalculation TenBitComparison BitDepthComparison BitDepthGrowth LuminancePerception RGBtoYCbCr


class BitDepth(Scene):
    def construct(self):

        # Create axes
        axes = Axes(
            x_range=[0, 5, 1],
            y_range=[0, 3, 1],
            x_length=8,
            y_length=4,
            axis_config={"color": WHITE},
        )

        # Create dimension labels
        x_label = Text("1920", font_size=24)
        y_label = Text("1080", font_size=24)
        x_label.next_to(axes.x_axis.get_end(), DOWN)
        y_label.next_to(axes.y_axis.get_end(), LEFT)

        self.play(Create(axes), Write(x_label), Write(y_label))
        self.wait(1)

        # Load and display the example image
        example_image = ImageMobject("imgs/beach2.png")
        # Set height to match the y-axis range while maintaining aspect ratio
        example_image.set_height(4)
        # Move image up slightly
        example_image.move_to(axes.get_center() + UP * 0.5)

        # Show the image first
        self.play(FadeIn(example_image))

        # Add initial explanation
        initial_explanation = Text(
            "Every digital image is made up of pixels", font_size=24
        )
        initial_explanation.to_edge(DOWN)
        self.play(Write(initial_explanation))
        self.wait(1)

        self.play(FadeOut(example_image), FadeOut(initial_explanation))
        self.wait(0.5)

        # Create a simplified grid of pixels (4x3 for demonstration)
        pixel_values = VGroup()

        first_pxl = True
        first_pxl_value = None
        for i in range(4):
            for j in range(3):
                # Create RGB values
                r = random.randint(0, 255)
                g = random.randint(0, 255)
                b = random.randint(0, 255)

                if first_pxl:
                    first_pxl_value = [r, g, b]
                    first_pxl = False

                # Create RGB dots with actual RGB colors
                rgb_dots = VGroup()
                for value, color in [(r, "#FF0000"), (g, "#00FF00"), (b, "#0000FF")]:
                    dot = Dot(color=color, radius=0.15)  # Increased dot size
                    rgb_dots.add(dot)

                # Arrange dots horizontally with more space
                rgb_dots.arrange(RIGHT, buff=0.2)  # Increased space between dots
                # Adjust position: shift right and increase spacing between columns
                rgb_dots.move_to(axes.c2p(i * 1.2 + 0.8, j + 0.5) + UP * 0.2)

                # Create value text with larger font size
                value_text = Text(f"[{r}, {g}, {b}]", font_size=20)
                value_text.next_to(rgb_dots, DOWN, buff=0.15)

                pixel_values.add(rgb_dots, value_text)

        # Animate RGB dots and values appearing
        self.play(LaggedStart(*[Write(dot) for dot in pixel_values], lag_ratio=0.1))
        self.wait(1)

        # Add final explanation
        explanation = Text(
            "Each pixel contains 3 color values (R,G,B)",
            font_size=24,
        )
        explanation.to_edge(DOWN)
        self.play(Write(explanation))
        self.wait(2)

        # Select one pixel to highlight (let's use the middle one)
        selected_pixel = pixel_values[4]  # Middle pixel in 4x3 grid
        selected_pixel_center = selected_pixel.get_center()

        # Create a larger version of the selected pixel
        larger_pixel = VGroup()
        for dot in selected_pixel[0]:  # RGB dots
            larger_dot = dot.copy()
            larger_dot.scale(2)
            larger_pixel.add(larger_dot)

        # Scale up the value text
        larger_value = selected_pixel[1].copy()  # Value text
        larger_value.scale(1.5)
        larger_pixel.add(larger_value)

        # Center the larger pixel
        larger_pixel.move_to(ORIGIN)

        # Fade out everything except the selected pixel
        self.play(
            FadeOut(axes),
            FadeOut(x_label),
            FadeOut(y_label),
            FadeOut(explanation),
            *[FadeOut(p) for p in pixel_values if p != selected_pixel],
            selected_pixel.animate.scale(2).move_to(ORIGIN),
            run_time=2,
        )
        self.wait(2)

        text = Text(
            f"[{first_pxl_value[0]}, {first_pxl_value[1]}, {first_pxl_value[2]}]",
            font_size=36,
        )
        text.shift(DOWN)
        self.play(Write(text))
        self.wait(2)
        self.play(FadeOut(text), FadeOut(selected_pixel))

        self.wait(1)

        # Part 1: Everything is 0s and 1s
        title1 = Text("Everything in a computer is 0s and 1s", font_size=36)
        self.play(Write(title1))
        self.wait(1)

        # Create a cluster of random 0s and 1s
        binary_cluster = VGroup()
        for i in range(5):
            for j in range(5):
                bit = Text("0" if random.random() < 0.5 else "1", font_size=24)
                bit.move_to([i - 2, j - 2, 0])
                binary_cluster.add(bit)

        self.play(FadeOut(title1), FadeIn(binary_cluster))
        self.wait(1)
        self.play(FadeOut(binary_cluster))
        # Part 2.5: What is a bit?
        bit_title = Text("What is a bit?", font_size=36)
        self.play(Write(bit_title))
        self.wait(1)
        self.play(FadeOut(bit_title))

        # Create a single bit demonstration
        bit_box = Square(side_length=0.8)
        bit_box.set_fill(WHITE, opacity=0.2)
        bit_box.set_stroke(WHITE, width=2)

        # Create both possible bit values
        bit_0 = Text("0", font_size=36)
        bit_0.move_to(bit_box.get_center())
        bit_1 = Text("1", font_size=36)
        bit_1.move_to(bit_box.get_center())

        # Show the bit box
        self.play(Create(bit_box))

        # Animate switching between 0 and 1
        self.play(Write(bit_0))
        self.wait(0.5)
        self.play(Transform(bit_0, bit_1))
        self.wait(0.5)
        self.play(Transform(bit_1, bit_0))
        self.wait(0.5)

        # Add explanation
        explanation = Text(
            "A bit can be either 0 or 1\n(2 possible values)", font_size=24
        )
        explanation.next_to(bit_box, DOWN, buff=0.5)
        self.play(Write(explanation))
        self.wait(2)

        # Clean up
        self.play(
            FadeOut(bit_box), FadeOut(bit_0), FadeOut(bit_1), FadeOut(explanation)
        )

        # Part 2: How these represent colors
        title2 = Text("How do these 0s and 1s represent colors?", font_size=36)
        self.play(FadeOut(binary_cluster), Write(title2))
        self.wait(1)
        self.play(FadeOut(title2))

        # Create 8 bit boxes with random initial values
        bits = []
        bit_boxes = []
        twos = VGroup()
        initial_values = [random.choice(["0", "1"]) for _ in range(8)]

        # Create the equals sign in a fixed position
        equals = Text("= 0-1", font_size=36)
        equals.shift(RIGHT * 6)  # Moved further right

        # Add title above the equals sign
        color_title = Text("Color values", font_size=24)
        color_title.next_to(equals, UP, buff=0.5)

        self.add(equals, color_title)

        # Show first bit and its value
        box = Square(side_length=0.8)
        box.set_fill(WHITE, opacity=0.2)
        box.set_stroke(WHITE, width=2)
        box.shift(LEFT * (3.5 - 0))
        bit = Text(initial_values[0], font_size=36)
        bit.move_to(box.get_center())
        bits.append(bit)
        bit_boxes.append(box)

        two = Text("2", font_size=36)
        two.next_to(box, UP)
        twos.add(two)

        self.play(Create(box), Write(bit), Write(two))

        for i in range(1, 8):  # Start from 1 since we already showed the first bit
            # Update the equals sign value before showing the next bit
            max_value = 2**i - 1
            new_equals = Text(f"= 0-{max_value}", font_size=36)
            new_equals.move_to(equals.get_center())
            self.play(
                FadeOut(equals), FadeIn(new_equals)
            )  # Combined into one play call
            equals = new_equals

            # Show the multiplication sign for the next step
            if i < 7:
                times = Text("×", font_size=36)
                times.next_to(twos[-1], RIGHT)
                self.play(Write(times))
                twos.add(times)

            # Now show the next bit
            box = Square(side_length=0.8)
            box.set_fill(WHITE, opacity=0.2)
            box.set_stroke(WHITE, width=2)
            box.shift(LEFT * (3.5 - i))
            bit = Text(initial_values[i], font_size=36)
            bit.move_to(box.get_center())
            bits.append(bit)
            bit_boxes.append(box)

            two = Text("2", font_size=36)
            two.next_to(box, UP)
            twos.add(two)

            self.play(Create(box), Write(bit), Write(two))

        # Add 8-bit title centered
        bit_depth_title = Text("8-bit", font_size=36)
        bit_depth_title.move_to(ORIGIN + DOWN * 2)

        self.play(Write(bit_depth_title))
        self.wait(1)

        # Update to final value
        final_equals = Text("= 0-255", font_size=36)
        final_equals.move_to(equals.get_center())
        self.play(FadeOut(equals), FadeIn(final_equals))
        self.wait(1)

        # Part 5: Show RGB squares with values
        self.play(
            FadeOut(twos),
            FadeOut(final_equals),
            FadeOut(color_title),
            FadeOut(bit_depth_title),
            FadeOut(VGroup(*bits)),
            FadeOut(VGroup(*bit_boxes)),
        )

        # Create RGB squares
        red_square = Square(side_length=2)
        red_square.set_fill("#FF0000", opacity=1)
        red_square.shift(LEFT * 4)

        green_square = Square(side_length=2)
        green_square.set_fill("#00FF00", opacity=1)

        blue_square = Square(side_length=2)
        blue_square.set_fill("#0000FF", opacity=1)
        blue_square.shift(RIGHT * 4)

        # Add value labels
        red_value = Text("0-255", font_size=36)
        red_value.next_to(red_square, DOWN)

        green_value = Text("0-255", font_size=36)
        green_value.next_to(green_square, DOWN)

        blue_value = Text("0-255", font_size=36)
        blue_value.next_to(blue_square, DOWN)

        self.play(
            Create(red_square),
            Create(green_square),
            Create(blue_square),
            Write(red_value),
            Write(green_value),
            Write(blue_value),
        )

        # Final explanation
        final_text = Text(
            "Each color channel (R,G,B) can have 256 different values",
            font_size=36,
        )
        final_text.to_edge(DOWN)
        self.play(Write(final_text))
        self.wait(2)
        self.play(
            FadeOut(final_text),
            FadeOut(red_square),
            FadeOut(green_square),
            FadeOut(blue_square),
            FadeOut(red_value),
            FadeOut(green_value),
            FadeOut(blue_value),
        )

        # Part 6: 10-bit Color Depth
        title1 = Text("8-bit Color Depth", font_size=36)
        title1.to_edge(UP)  # Move title to top
        self.play(Write(title1))
        self.wait(1)

        # Create 8 bit boxes with random initial values
        bits_8 = []
        bit_boxes_8 = []
        initial_values = [random.choice(["0", "1"]) for _ in range(8)]
        for i in range(8):
            box = Square(side_length=0.8)
            box.set_fill(WHITE, opacity=0.2)
            box.set_stroke(WHITE, width=2)
            box.shift(LEFT * (5.5 - i))
            bit = Text(initial_values[i], font_size=36)
            bit.move_to(box.get_center())
            bits_8.append(bit)
            bit_boxes_8.append(box)
            self.play(Create(box), Write(bit))

        # Show 8-bit calculation
        twos_8 = VGroup()
        for i in range(8):
            two = Text("2", font_size=36)
            two.next_to(bit_boxes_8[i], UP, buff=1.5)  # Increased buffer space
            if i < 7:
                times = Text("×", font_size=36)
                times.next_to(two, RIGHT)
                twos_8.add(two, times)
            else:
                twos_8.add(two)

        equals_8 = Text("= 256", font_size=36)
        equals_8.next_to(twos_8, RIGHT)

        self.play(Write(twos_8), Write(equals_8))
        self.wait(1)
        self.play(FadeOut(title1))

        # Transition to 10-bit
        title2 = Text("10-bit Color Depth", font_size=36)
        title2.to_edge(UP)  # Move title to top
        self.play(FadeOut(twos_8), FadeOut(equals_8), Write(title2))
        self.wait(1)
        self.play(FadeOut(title2))

        # Create 10 bit boxes (reusing first 8, adding 2 more)
        bits_10 = bits_8.copy()
        bit_boxes_10 = bit_boxes_8.copy()

        # Add two more bits
        for i in range(8, 10):
            box = Square(side_length=0.8)
            box.set_fill(GREEN, opacity=0.2)
            box.set_stroke(GREEN, width=2)
            box.shift(LEFT * (5.5 - i))
            bit = Text(random.choice(["0", "1"]), font_size=36)
            bit.move_to(box.get_center())
            bits_10.append(bit)
            bit_boxes_10.append(box)
            self.play(Create(box), Write(bit))

        # Show 10-bit calculation
        twos_10 = VGroup()
        for i in range(10):
            two = Text("2", font_size=36)
            two.next_to(bit_boxes_10[i], UP, buff=1.5)  # Increased buffer space
            if i < 9:
                times = Text("×", font_size=36)
                times.next_to(two, RIGHT)
                twos_10.add(two, times)
            else:
                twos_10.add(two)

        equals_10 = Text("= 1024", font_size=36)
        equals_10.next_to(twos_10, RIGHT)

        self.play(Write(twos_10), Write(equals_10))
        self.wait(1)
        # Memory calculation
        eight_bit_calc = Text(
            "8-bit: 1920 × 1080 × 3 channels × 8 bits = 49,766,400 bits\n" "= 6.22 MB",
            font_size=32,
        )
        eight_bit_calc.next_to(ORIGIN, DOWN * 3, buff=0.5)

        ten_bit_calc = Text(
            "10-bit: 1920 × 1080 × 3 channels × 10 bits = 62,208,000 bits\n"
            "= 7.78 MB",
            font_size=32,
        )
        ten_bit_calc.next_to(eight_bit_calc, DOWN, buff=0.5)
        self.play(Write(eight_bit_calc))
        self.wait(1)
        self.play(Write(ten_bit_calc))
        self.wait(1)

        # Memory comparison
        self.play(
            FadeOut(VGroup(*bits_10)),
            FadeOut(VGroup(*bit_boxes_10)),
            FadeOut(twos_10),
            FadeOut(equals_10),
            FadeOut(eight_bit_calc),
            FadeOut(ten_bit_calc),
        )

        # Create 8-bit value range
        title = Text("8-bit vs 10-bit size", font_size=28)
        title.to_edge(UP)

        eight_bit_values = VGroup()
        for i in range(8):  # Show 8 representative values
            value = Square(side_length=0.3, color=BLUE)  # Smaller squares
            value.set_fill(BLUE, opacity=0.3)
            value.shift(LEFT * 6 + RIGHT * i * 0.4 + UP * 2)  # Centered horizontally
            eight_bit_values.add(value)

        # Create a horizontal line of squares for 8-bit
        eight_bit_title = Text("8-bit", font_size=24)
        eight_bit_title.next_to(eight_bit_values, UP, buff=0.3)
        eight_bit_title.align_to(
            eight_bit_values, LEFT
        )  # Align with left edge of squares

        # Add start and end values
        eight_bit_range = Text("0 → 255", font_size=20)
        eight_bit_range.next_to(eight_bit_values, DOWN, buff=0.3)

        self.play(
            Write(title),
            Write(eight_bit_title),
            Create(eight_bit_values),
            Write(eight_bit_range),
            run_time=3,
        )
        self.wait(1)

        # Create additional squares for 10-bit
        ten_bit_extension = VGroup()
        for i in range(32):  # Show 32 squares for 10-bit
            value = Square(side_length=0.3, color=GREEN)  # Same size as 8-bit squares
            value.set_fill(GREEN, opacity=0.3)
            value.shift(LEFT * 6 + RIGHT * i * 0.4)  # Centered horizontally
            ten_bit_extension.add(value)

        # Create 10-bit by extending the 8-bit range
        ten_bit_title = Text("10-bit", font_size=24)
        ten_bit_title.next_to(ten_bit_extension, UP, buff=0.3)
        ten_bit_title.shift(LEFT * 6)  # Align with left edge of squares

        # Add start and end values
        ten_bit_range = Text("0 → 1023", font_size=20)
        ten_bit_range.next_to(ten_bit_extension, DOWN, buff=0.3)

        self.play(
            Write(ten_bit_title),
            Create(ten_bit_extension),
            Write(ten_bit_range),
            run_time=3,
        )
        self.wait(1)

        # Show storage comparison
        storage_title = Text("Storage Size Comparison 1920x1080", font_size=28)
        storage_title.next_to(ten_bit_range, DOWN, buff=0.5)
        self.play(Write(storage_title))

        # Create storage comparison
        eight_bit_storage = Rectangle(
            width=2, height=1, color=BLUE
        )  # Smaller rectangles
        eight_bit_storage.set_fill(BLUE, opacity=0.3)
        eight_bit_storage.next_to(storage_title, DOWN, buff=0.5)
        eight_bit_storage.shift(LEFT * 1.2)
        eight_bit_label = Text("6.22 MB", font_size=20, color=BLUE)
        eight_bit_label.move_to(eight_bit_storage)

        ten_bit_storage = Rectangle(
            width=2.5, height=1, color=GREEN
        )  # Smaller rectangles
        ten_bit_storage.set_fill(GREEN, opacity=0.3)
        ten_bit_storage.next_to(eight_bit_storage, RIGHT, buff=0.6)
        ten_bit_label = Text("7.78 MB", font_size=20, color=GREEN)
        ten_bit_label.move_to(ten_bit_storage)

        self.play(
            Create(eight_bit_storage),
            Write(eight_bit_label),
            Create(ten_bit_storage),
            Write(ten_bit_label),
        )

        # Add comparison text
        storage_text = Text("25% more storage - 4x more color values", font_size=28)
        storage_text.next_to(eight_bit_storage, DOWN, buff=0.3)
        storage_text.align_to(storage_title, LEFT)  # Align with storage title

        self.play(Write(storage_text))
        self.wait(2)
        self.play(
            FadeOut(storage_text),
            FadeOut(storage_title),
            FadeOut(eight_bit_label),
            FadeOut(ten_bit_label),
            FadeOut(eight_bit_values),
            FadeOut(ten_bit_extension),
            FadeOut(eight_bit_title),
            FadeOut(ten_bit_title),
            FadeOut(eight_bit_range),
            FadeOut(ten_bit_range),
            FadeOut(eight_bit_storage),
            FadeOut(ten_bit_storage),
        )

        # First line: Show complete calculation
        calculation = Text(
            "1920 × 1080 × 3 (RGB) × 8 (bits) = 49,766,400 bits", font_size=28
        )
        calculation.shift(UP * 3)  # Center horizontally
        self.play(Write(calculation))
        self.wait(1)

        # Second line: Show bits to bytes conversion
        bits_to_bytes = Text("8 bits = 1 byte", font_size=28)
        bits_to_bytes.next_to(calculation, DOWN, buff=0.5)
        bits_to_bytes.align_to(calculation, LEFT)
        self.play(Write(bits_to_bytes))
        self.wait(1)

        # Third line: Show bytes calculation
        bytes_calc = Text("49,766,400 ÷ 8 = 6,220,800 bytes", font_size=28)
        bytes_calc.next_to(bits_to_bytes, DOWN, buff=0.5)
        bytes_calc.align_to(calculation, LEFT)
        self.play(Write(bytes_calc))
        self.wait(1)

        # Add explanation about M
        mega_explanation = Text("M = Mega = 1,000,000", font_size=28)
        mega_explanation.next_to(bytes_calc, DOWN, buff=0.5)
        mega_explanation.align_to(calculation, LEFT)
        self.play(Write(mega_explanation))
        self.wait(1)

        # Final line: Show megabytes
        mb_result = Text("= 6.22 MB", font_size=28, color=YELLOW)
        mb_result.next_to(mega_explanation, DOWN, buff=0.5)
        mb_result.align_to(calculation, LEFT)
        self.play(Write(mb_result))
        self.wait(1)

        # FPS calculations
        fps_title = Text("At 24 Frames Per Second:", font_size=28)
        fps_title.next_to(mb_result, DOWN, buff=0.8)
        fps_title.align_to(calculation, LEFT)
        self.play(Write(fps_title))
        self.wait(1)

        # Bytes per second
        bytes_per_second = Text("6.22 MB × 24 = 149 MB/s", font_size=28)
        bytes_per_second.next_to(fps_title, DOWN, buff=0.5)
        bytes_per_second.align_to(calculation, LEFT)
        self.play(Write(bytes_per_second))
        self.wait(1)

        # Bits per second
        bits_per_second = Text("149 MB × 8 = 1200 Mbits/s", font_size=28)
        bits_per_second.next_to(bytes_per_second, DOWN, buff=0.5)
        bits_per_second.align_to(calculation, LEFT)
        self.play(Write(bits_per_second))
        self.wait(1)

        # Internet speed comparison
        internet_speed = Text(
            "Typical home internet: 100-1000 Mbits/s", font_size=28, color=RED
        )
        internet_speed.next_to(bits_per_second, DOWN, buff=0.8)
        internet_speed.align_to(calculation, LEFT)
        self.play(Write(internet_speed))
        self.wait(2)

        # Show the conversion calculations
        # Clear previous elements
        conversion_title = Text("BT.709 Conversion", font_size=36)
        conversion_title.to_edge(UP)
        self.play(Write(conversion_title))

        # Create the RGB values
        rgb_values = Text("R = 180, G = 140, B = 120", font_size=28).next_to(
            conversion_title, DOWN, buff=1
        )
        self.play(Write(rgb_values))
        self.wait(1)

        # Python code for conversion
        code_comment = Text("# Rec. 709 conversion matrix", font_size=28)

        # Create the Y calculation with colored RGB references
        y_code_start = Text("y = 0.2126 * ", font_size=28)
        y_rgb_r = Text("rgb[:, :, 0]", font_size=28, color=RED)
        y_plus1 = Text(" + 0.7152 * ", font_size=28)
        y_rgb_g = Text("rgb[:, :, 1]", font_size=28, color=GREEN)
        y_plus2 = Text(" + 0.0722 * ", font_size=28)
        y_rgb_b = Text("rgb[:, :, 2]", font_size=28, color=BLUE)

        y_line = VGroup(
            y_code_start, y_rgb_r, y_plus1, y_rgb_g, y_plus2, y_rgb_b
        ).arrange(RIGHT, buff=0)

        # Create the Cb calculation with colored RGB
        cb_code_start = Text("cb = 0.5 * (", font_size=28)
        cb_rgb = Text("rgb[:, :, 2]", font_size=28, color=BLUE)
        cb_end = Text(" - y) / (1 - 0.0722)  # Blue difference", font_size=28)

        cb_line = VGroup(cb_code_start, cb_rgb, cb_end).arrange(RIGHT, buff=0)

        # Create the Cr calculation with colored RGB
        cr_code_start = Text("cr = 0.5 * (", font_size=28)
        cr_rgb = Text("rgb[:, :, 0]", font_size=28, color=RED)
        cr_end = Text(" - y) / (1 - 0.2126)  # Red difference", font_size=28)

        cr_line = VGroup(cr_code_start, cr_rgb, cr_end).arrange(RIGHT, buff=0)

        # Arrange all code lines
        code_group = VGroup(code_comment, y_line, cb_line, cr_line).arrange(
            DOWN, buff=0.5, aligned_edge=LEFT
        )

        code_group.next_to(rgb_values, DOWN, buff=1)

        # Animate code appearing
        self.play(Write(code_comment))
        self.wait(0.5)

        self.play(Write(y_line))
        self.wait(1)

        self.play(Write(cb_line))
        self.wait(1)

        self.play(Write(cr_line))
        self.wait(1)

        # Show final YCbCr values
        final_values = Text(
            "Final YCbCr: (147, -15, 21)", font_size=32, color=YELLOW
        ).next_to(code_group, DOWN, buff=1)

        self.play(Write(final_values))
        self.wait(2)

        # Now explain why we use these coefficients
        self.play(
            FadeOut(conversion_title),
            FadeOut(rgb_values),
            FadeOut(code_group),
            FadeOut(final_values),
        )
        self.wait(0.5)

        # Show color coefficients
        coef_title = Text(
            "Why These Numbers? Color Sensitivity in Human Vision:", font_size=32
        )
        coef_title.to_edge(UP)
        self.play(Write(coef_title))

        # Create RGB circles first
        circles_group = VGroup()

        circleRed = Circle(radius=0.4)  # create a circle
        circleRed.set_fill("#FF0000", opacity=1)  # pure red
        circleRed.set_stroke(width=0)  # set the stroke width

        circleGreen = Circle(radius=0.4)  # create a circle
        circleGreen.set_fill("#00FF00", opacity=1)  # pure green
        circleGreen.set_stroke(width=0)  # set the stroke width

        circleBlue = Circle(radius=0.4)  # create a circle
        circleBlue.set_fill("#0000FF", opacity=1)  # pure blue
        circleBlue.set_stroke(width=0)  # set the stroke width

        circles_group.add(circleGreen, circleRed, circleBlue)
        circles_group.arrange(RIGHT, buff=2)
        circles_group.next_to(coef_title, DOWN, buff=1)

        # Create percentage bars and labels
        green_percent = Text("72%", font_size=36, color=GREEN)
        red_percent = Text("21%", font_size=36, color=RED)
        blue_percent = Text("7%", font_size=36, color=BLUE)

        # Position percentages under their respective circles
        green_percent.next_to(circleGreen, DOWN, buff=0.3)
        red_percent.next_to(circleRed, DOWN, buff=0.3)
        blue_percent.next_to(circleBlue, DOWN, buff=0.3)

        # Add color labels above circles
        green_label = Text("GREEN", font_size=28, color=GREEN)
        red_label = Text("RED", font_size=28, color=RED)
        blue_label = Text("BLUE", font_size=28, color=BLUE)

        green_label.next_to(circleGreen, UP, buff=0.3)
        red_label.next_to(circleRed, UP, buff=0.3)
        blue_label.next_to(circleBlue, UP, buff=0.3)

        # Show coefficients with animation sequence
        self.play(Write(coef_title))
        self.wait(0.5)

        # Show circles first
        self.play(Create(circleGreen), Create(circleRed), Create(circleBlue))
        self.wait(1)

        # Then show labels and percentages for each color
        for circle, label, percent in zip(
            [circleGreen, circleRed, circleBlue],
            [green_label, red_label, blue_label],
            [green_percent, red_percent, blue_percent],
        ):
            self.play(Write(label), Write(percent))
            self.wait(0.5)

        # Add explanation about green brightness
        brightness_explanation = Text(
            "Notice how the green circle appears brighter to our eyes", font_size=24
        )
        brightness_explanation.next_to(circles_group, DOWN, buff=1.5)
        self.play(Write(brightness_explanation))
        self.wait(2)

        # Fade out everything
        self.play(
            FadeOut(coef_title),
            FadeOut(circles_group),
            FadeOut(green_label),
            FadeOut(red_label),
            FadeOut(blue_label),
            FadeOut(green_percent),
            FadeOut(red_percent),
            FadeOut(blue_percent),
            FadeOut(brightness_explanation),
        )
        self.wait(0.5)

        # Show 4:4:4
        format_444_label = Text("4:4:4 - Full Resolution", font_size=36)
        format_444_label.to_edge(UP)
        self.play(Write(format_444_label))

        axes_444 = Axes(
            x_range=[0, 5, 1],
            y_range=[0, 3, 1],
            x_length=8,
            y_length=4,
            axis_config={"color": WHITE},
        )

        x_label_444 = Text("1920", font_size=24)
        y_label_444 = Text("1080", font_size=24)
        x_label_444.next_to(axes_444.x_axis.get_end(), DOWN)
        y_label_444.next_to(axes_444.y_axis.get_end(), LEFT)

        self.play(Create(axes_444), Write(x_label_444), Write(y_label_444))
        pixel_values_444 = create_ycbcr_grid(self, axes_444, full=True)
        self.wait(3)  # Show 444 for 3 seconds

        # Remove 4:4:4 completely
        self.play(
            *[
                FadeOut(mob)
                for mob in [
                    format_444_label,
                    axes_444,
                    x_label_444,
                    y_label_444,
                    pixel_values_444,
                ]
            ]
        )
        self.wait(1)  # Clear pause between formats

        # Show 4:2:2
        format_422_label = Text(
            "4:2:2 - Half Horizontal Color Resolution", font_size=36
        )
        format_422_label.to_edge(UP)
        self.play(Write(format_422_label))

        axes_422 = Axes(
            x_range=[0, 5, 1],
            y_range=[0, 3, 1],
            x_length=8,
            y_length=4,
            axis_config={"color": WHITE},
        )

        x_label_422 = Text("1920", font_size=24)
        y_label_422 = Text("1080", font_size=24)
        x_label_422.next_to(axes_422.x_axis.get_end(), DOWN)
        y_label_422.next_to(axes_422.y_axis.get_end(), LEFT)

        self.play(Create(axes_422), Write(x_label_422), Write(y_label_422))
        pixel_values_422 = create_ycbcr_grid(self, axes_422, horizontal_subsample=True)
        self.wait(3)  # Show 422 for 3 seconds

        # Remove 4:2:2 completely
        self.play(
            *[
                FadeOut(mob)
                for mob in [
                    format_422_label,
                    axes_422,
                    x_label_422,
                    y_label_422,
                    pixel_values_422,
                ]
            ]
        )
        self.wait(1)  # Clear pause between formats

        # Show 4:2:0
        format_420_label = Text("4:2:0 - Quarter Color Resolution", font_size=36)
        format_420_label.to_edge(UP)
        self.play(Write(format_420_label))

        axes_420 = Axes(
            x_range=[0, 5, 1],
            y_range=[0, 3, 1],
            x_length=8,
            y_length=4,
            axis_config={"color": WHITE},
        )

        x_label_420 = Text("1920", font_size=24)
        y_label_420 = Text("1080", font_size=24)
        x_label_420.next_to(axes_420.x_axis.get_end(), DOWN)
        y_label_420.next_to(axes_420.y_axis.get_end(), LEFT)

        self.play(Create(axes_420), Write(x_label_420), Write(y_label_420))
        pixel_values_420 = create_ycbcr_grid(
            self, axes_420, horizontal_subsample=True, vertical_subsample=True
        )
        self.wait(3)  # Show 420 for 3 seconds

        # Add final explanation
        final_explanation = Text(
            "4:2:0 is most common - used in H.264, H.265, and streaming video",
            font_size=24,
        )
        final_explanation.to_edge(DOWN)
        self.play(Write(final_explanation))
        self.wait(2)

        # Clear everything before showing difference image
        self.play(
            *[
                FadeOut(mob)
                for mob in [
                    format_420_label,
                    axes_420,
                    x_label_420,
                    y_label_420,
                    pixel_values_420,
                    final_explanation,
                ]
            ]
        )
        self.wait(1)

        # Show subsampling difference image
        diff_title = Text("Subsampling Difference Visualization (×10)", font_size=36)
        diff_title.to_edge(UP)
        self.play(Write(diff_title))

        diff_image = ImageMobject("imgs/subsampling-diff.png")
        # Set height to match previous image size while maintaining aspect ratio
        diff_image.set_width(14)  # Set to frame width with margin
        diff_image.move_to(ORIGIN)

        self.play(FadeIn(diff_image))
        self.wait(3)


def create_ycbcr_grid(
    scene, axes, full=False, horizontal_subsample=False, vertical_subsample=False
):
    pixel_values = VGroup()

    for i in range(4):  # columns
        for j in range(3):  # rows
            # Create YCbCr values
            y_val = random.randint(16, 235)  # Y range in digital

            # Determine if this position should have color information
            has_color = True
            if (
                horizontal_subsample and i % 2 == 1
            ):  # Skip odd columns for 4:2:2 and 4:2:0
                has_color = False
            if vertical_subsample and j % 2 == 1:  # Skip odd rows for 4:2:0
                has_color = False

            if has_color:
                cb_val = random.randint(16, 240) - 128  # Cb range centered around 0
                cr_val = random.randint(16, 240) - 128  # Cr range centered around 0

            # Create dots group
            dots = VGroup()

            # Always add Y (luminance)
            y_dot = Dot(color="#FFFFFF", radius=0.15)
            dots.add(y_dot)

            if has_color:
                # Add Cb and Cr for positions that should have color
                cb_dot = Dot(color="#0000FF", radius=0.15)
                cr_dot = Dot(color="#FF0000", radius=0.15)
                dots.add(cb_dot, cr_dot)
                value_text = Text(f"[{y_val}, {cb_val:+}, {cr_val:+}]", font_size=20)
            else:
                # Add X marks for missing color information
                cb_x = Text("×", font_size=24, color=GRAY).scale(1.2)
                cr_x = Text("×", font_size=24, color=GRAY).scale(1.2)
                dots.add(cb_x, cr_x)
                value_text = Text(f"[{y_val}, ×, ×]", font_size=20)

            # Arrange dots horizontally
            dots.arrange(RIGHT, buff=0.2)
            dots.move_to(axes.c2p(i * 1.2 + 0.8, j + 0.5) + UP * 0.2)

            # Position value text
            value_text.next_to(dots, DOWN, buff=0.15)

            pixel_values.add(dots, value_text)

    # Animate grid appearing
    scene.play(LaggedStart(*[Write(dot) for dot in pixel_values], lag_ratio=0.1))

    return pixel_values


class YCbCr(Scene):
    def construct(self):
        # Title
        title = Text("Human Vision: Luminance vs Color", font_size=36)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # Load the beach image
        beach_img = ImageMobject("imgs/beach2.png")
        beach_img.set_height(6)  # Make it larger for better visibility
        beach_img.move_to(ORIGIN)

        # Create highlighting rectangles
        face_rect = Rectangle(
            width=2, height=2.2, stroke_color=YELLOW, stroke_width=3, fill_opacity=0
        )
        face_rect.move_to(
            beach_img.get_center() + UP * 1.5 + LEFT * 0.5
        )  # Moved higher up and left

        background_rect = Rectangle(
            width=5,
            height=2.5,  # Made slightly larger to cover more of the sky/ocean
            stroke_color=BLUE,
            stroke_width=3,
            fill_opacity=0,
        )
        background_rect.move_to(
            beach_img.get_center() + UP * 2.5 + RIGHT * 3.2
        )  # Moved to upper portion

        # Show original image
        self.play(FadeIn(beach_img))
        self.wait(1)

        # Add explanation about luminance
        explanation1 = Text(
            "Humans are more sensitive to light/dark differences\nthan to color variations",
            font_size=24,
        )
        explanation1.next_to(beach_img, DOWN, buff=0.5)
        self.play(Write(explanation1))
        self.wait(1)

        # First highlight face region
        face_label = Text("Face: Rich in luminance detail", font_size=24, color=WHITE)
        face_label.next_to(face_rect, RIGHT, buff=0.5)

        self.play(Create(face_rect), Write(face_label))
        self.wait(2)  # Longer pause on face highlight

        # Fade out face highlight before showing background
        self.play(FadeOut(face_rect), FadeOut(face_label))
        self.wait(0.5)

        # Then highlight background region
        bg_label = Text("Background: Mostly color variation", font_size=24, color=WHITE)
        bg_label.next_to(background_rect, LEFT, buff=0.5)

        self.play(Create(background_rect), Write(bg_label))
        self.wait(2)  # Longer pause on background highlight
        self.play(
            FadeOut(background_rect),
            FadeOut(bg_label),
            FadeOut(beach_img),
            FadeOut(explanation1),
            FadeOut(title),
        )
        # Start with the problem statement
        problem = Text(
            "Problem: How can we compress color\nwhile preserving luminance?",
            font_size=40,
        ).move_to(ORIGIN)

        self.play(Write(problem))
        self.wait(2)
        self.play(FadeOut(problem))
        self.wait(0.5)

        # Create a single pixel representation
        pixel_group = VGroup()

        # Generate some interesting RGB values that will show good luminance
        r, g, b = 180, 140, 120  # Skin tone-like color

        # Create RGB dots with actual RGB colors
        rgb_dots = VGroup()
        for value, color, label in [
            (r, "#FF0000", "R"),
            (g, "#00FF00", "G"),
            (b, "#0000FF", "B"),
        ]:
            dot = Dot(color=color, radius=0.2)
            # Add label above dot
            label_text = Text(label, font_size=24).next_to(dot, UP, buff=0.2)
            # Add value below dot
            value_text = Text(str(value), font_size=24).next_to(dot, DOWN, buff=0.2)
            rgb_dots.add(VGroup(dot, label_text, value_text))

        # Arrange dots horizontally with more space
        rgb_dots.arrange(RIGHT, buff=1)
        rgb_dots.move_to(ORIGIN)

        # Create the combined color preview
        combined_color = f"#{r:02x}{g:02x}{b:02x}"
        color_preview = Square(
            side_length=1, fill_color=combined_color, fill_opacity=1, stroke_width=0
        )
        color_preview.next_to(rgb_dots, UP, buff=1)

        # Add "Combined Color" label
        preview_label = Text("Combined Color", font_size=24)
        preview_label.next_to(color_preview, UP, buff=0.3)

        # Create explanation text
        explanation = Text(
            "In RGB, color and brightness information are mixed together", font_size=24
        )
        explanation.next_to(rgb_dots, DOWN, buff=1)

        # Animate everything appearing
        self.play(FadeIn(color_preview), Write(preview_label))
        self.wait(1)

        self.play(*[Write(dot_group) for dot_group in rgb_dots], run_time=2)
        self.wait(1)

        self.play(Write(explanation))
        self.wait(2)

        # Fade out all RGB elements
        self.play(
            FadeOut(color_preview),
            FadeOut(preview_label),
            FadeOut(rgb_dots),
            FadeOut(explanation),
        )
        self.wait(1)

        # Show the solution with separators
        solution_text = Text("Solution:", font_size=36).move_to(ORIGIN + UP * 1.5)

        # Create YCrCb components with separators
        components = VGroup()
        for component, color in [
            ("Y", WHITE),
            ("|", GRAY),
            ("Cb", BLUE),
            ("|", GRAY),
            ("Cr", RED),
        ]:
            text = Text(component, font_size=36, color=color)
            components.add(text)

        # Increase spacing between components
        components.arrange(RIGHT, buff=1.5)  # Increased from 0.8
        components.next_to(solution_text, DOWN, buff=1)

        # Add component labels with more space
        y_label = Text("(Luminance)", font_size=24, color=WHITE)
        cb_label = Text("(Blue Difference)", font_size=24, color=BLUE)
        cr_label = Text("(Red Difference)", font_size=24, color=RED)

        # Position labels under their respective components with more vertical space
        y_label.next_to(components[0], DOWN, buff=0.5)
        cb_label.next_to(components[2], DOWN, buff=0.5)
        cr_label.next_to(components[4], DOWN, buff=0.5)

        # Shift the entire component group up to make room for labels
        components.shift(UP * 0.5)

        # Animate solution appearing
        self.play(Write(solution_text))
        self.wait(0.5)

        # Animate components appearing one by one with their labels
        self.play(Write(components[0]), Write(y_label))
        self.wait(0.5)
        self.play(Write(components[1]))
        self.wait(0.2)
        self.play(Write(components[2]), Write(cb_label))
        self.wait(0.5)
        self.play(Write(components[3]))
        self.wait(0.2)
        self.play(Write(components[4]), Write(cr_label))
        self.wait(2)

        # Show YCbCr image
        ycbcr_img = ImageMobject("imgs/ycbcr.png")
        ycbcr_img.set_width(14)  # Set to frame width with margin
        ycbcr_img.move_to(ORIGIN)

        # Fade out text temporarily
        self.play(
            FadeOut(solution_text),
            FadeOut(components),
            FadeOut(y_label),
            FadeOut(cb_label),
            FadeOut(cr_label),
        )

        # Show the image
        self.play(FadeIn(ycbcr_img))
        self.wait(2)  # Show image for 2 seconds
        self.play(FadeOut(ycbcr_img))
        self.wait(0.5)

        # Show the conversion calculations
        # Clear previous elements
        conversion_title = Text("BT.709 Conversion", font_size=36)
        conversion_title.to_edge(UP)
        self.play(Write(conversion_title))

        # Create the RGB values
        rgb_values = Text("R = 180, G = 140, B = 120", font_size=28).next_to(
            conversion_title, DOWN, buff=1
        )
        self.play(Write(rgb_values))
        self.wait(1)

        # Python code for conversion
        code_comment = Text("# Rec. 709 conversion matrix", font_size=28)

        # Create the Y calculation with colored RGB references
        y_code_start = Text("y = 0.2126 * ", font_size=28)
        y_rgb_r = Text("rgb[:, :, 0]", font_size=28, color=RED)
        y_plus1 = Text(" + 0.7152 * ", font_size=28)
        y_rgb_g = Text("rgb[:, :, 1]", font_size=28, color=GREEN)
        y_plus2 = Text(" + 0.0722 * ", font_size=28)
        y_rgb_b = Text("rgb[:, :, 2]", font_size=28, color=BLUE)

        y_line = VGroup(
            y_code_start, y_rgb_r, y_plus1, y_rgb_g, y_plus2, y_rgb_b
        ).arrange(RIGHT, buff=0)

        # Create the Cb calculation with colored RGB
        cb_code_start = Text("cb = 0.5 * (", font_size=28)
        cb_rgb = Text("rgb[:, :, 2]", font_size=28, color=BLUE)
        cb_end = Text(" - y) / (1 - 0.0722)  # Blue difference", font_size=28)

        cb_line = VGroup(cb_code_start, cb_rgb, cb_end).arrange(RIGHT, buff=0)

        # Create the Cr calculation with colored RGB
        cr_code_start = Text("cr = 0.5 * (", font_size=28)
        cr_rgb = Text("rgb[:, :, 0]", font_size=28, color=RED)
        cr_end = Text(" - y) / (1 - 0.2126)  # Red difference", font_size=28)

        cr_line = VGroup(cr_code_start, cr_rgb, cr_end).arrange(RIGHT, buff=0)

        # Arrange all code lines
        code_group = VGroup(code_comment, y_line, cb_line, cr_line).arrange(
            DOWN, buff=0.5, aligned_edge=LEFT
        )

        code_group.next_to(rgb_values, DOWN, buff=1)

        # Animate code appearing
        self.play(Write(code_comment))
        self.wait(0.5)

        self.play(Write(y_line))
        self.wait(1)

        self.play(Write(cb_line))
        self.wait(1)

        self.play(Write(cr_line))
        self.wait(1)

        # Show final YCbCr values
        final_values = Text(
            "Final YCbCr: (147, -15, 21)", font_size=32, color=YELLOW
        ).next_to(code_group, DOWN, buff=1)

        self.play(Write(final_values))
        self.wait(2)

        # Now explain why we use these coefficients
        self.play(
            FadeOut(conversion_title),
            FadeOut(rgb_values),
            FadeOut(code_group),
            FadeOut(final_values),
        )
        self.wait(0.5)

        # Show color coefficients
        coef_title = Text(
            "Why These Numbers? Color Sensitivity in Human Vision:", font_size=32
        )
        coef_title.to_edge(UP)
        self.play(Write(coef_title))

        # Create RGB circles first
        circles_group = VGroup()

        circleRed = Circle(radius=0.4)  # create a circle
        circleRed.set_fill("#FF0000", opacity=1)  # pure red
        circleRed.set_stroke(width=0)  # set the stroke width

        circleGreen = Circle(radius=0.4)  # create a circle
        circleGreen.set_fill("#00FF00", opacity=1)  # pure green
        circleGreen.set_stroke(width=0)  # set the stroke width

        circleBlue = Circle(radius=0.4)  # create a circle
        circleBlue.set_fill("#0000FF", opacity=1)  # pure blue
        circleBlue.set_stroke(width=0)  # set the stroke width

        circles_group.add(circleGreen, circleRed, circleBlue)
        circles_group.arrange(RIGHT, buff=2)
        circles_group.next_to(coef_title, DOWN, buff=1)

        # Create percentage bars and labels
        green_percent = Text("72%", font_size=36, color=GREEN)
        red_percent = Text("21%", font_size=36, color=RED)
        blue_percent = Text("7%", font_size=36, color=BLUE)

        # Position percentages under their respective circles
        green_percent.next_to(circleGreen, DOWN, buff=0.3)
        red_percent.next_to(circleRed, DOWN, buff=0.3)
        blue_percent.next_to(circleBlue, DOWN, buff=0.3)

        # Add color labels above circles
        green_label = Text("GREEN", font_size=28, color=GREEN)
        red_label = Text("RED", font_size=28, color=RED)
        blue_label = Text("BLUE", font_size=28, color=BLUE)

        green_label.next_to(circleGreen, UP, buff=0.3)
        red_label.next_to(circleRed, UP, buff=0.3)
        blue_label.next_to(circleBlue, UP, buff=0.3)

        # Show coefficients with animation sequence
        self.play(Write(coef_title))
        self.wait(0.5)

        # Show circles first
        self.play(Create(circleGreen), Create(circleRed), Create(circleBlue))
        self.wait(1)

        # Then show labels and percentages for each color
        for circle, label, percent in zip(
            [circleGreen, circleRed, circleBlue],
            [green_label, red_label, blue_label],
            [green_percent, red_percent, blue_percent],
        ):
            self.play(Write(label), Write(percent))
            self.wait(0.5)

        # Add explanation about green brightness
        brightness_explanation = Text(
            "Notice how the green circle appears brighter to our eyes", font_size=24
        )
        brightness_explanation.next_to(circles_group, DOWN, buff=1.5)
        self.play(Write(brightness_explanation))
        self.wait(2)

        # Fade out everything
        self.play(
            FadeOut(coef_title),
            FadeOut(circles_group),
            FadeOut(green_label),
            FadeOut(red_label),
            FadeOut(blue_label),
            FadeOut(green_percent),
            FadeOut(red_percent),
            FadeOut(blue_percent),
            FadeOut(brightness_explanation),
        )
        self.wait(0.5)

        # Show 4:4:4
        format_444_label = Text("4:4:4 - Full Resolution", font_size=36)
        format_444_label.to_edge(UP)
        self.play(Write(format_444_label))

        axes_444 = Axes(
            x_range=[0, 5, 1],
            y_range=[0, 3, 1],
            x_length=8,
            y_length=4,
            axis_config={"color": WHITE},
        )

        x_label_444 = Text("1920", font_size=24)
        y_label_444 = Text("1080", font_size=24)
        x_label_444.next_to(axes_444.x_axis.get_end(), DOWN)
        y_label_444.next_to(axes_444.y_axis.get_end(), LEFT)

        self.play(Create(axes_444), Write(x_label_444), Write(y_label_444))
        pixel_values_444 = create_ycbcr_grid(self, axes_444, full=True)
        self.wait(3)  # Show 444 for 3 seconds

        # Remove 4:4:4 completely
        self.play(
            *[
                FadeOut(mob)
                for mob in [
                    format_444_label,
                    axes_444,
                    x_label_444,
                    y_label_444,
                    pixel_values_444,
                ]
            ]
        )
        self.wait(1)  # Clear pause between formats

        # Show 4:2:2
        format_422_label = Text(
            "4:2:2 - Half Horizontal Color Resolution", font_size=36
        )
        format_422_label.to_edge(UP)
        self.play(Write(format_422_label))

        axes_422 = Axes(
            x_range=[0, 5, 1],
            y_range=[0, 3, 1],
            x_length=8,
            y_length=4,
            axis_config={"color": WHITE},
        )

        x_label_422 = Text("1920", font_size=24)
        y_label_422 = Text("1080", font_size=24)
        x_label_422.next_to(axes_422.x_axis.get_end(), DOWN)
        y_label_422.next_to(axes_422.y_axis.get_end(), LEFT)

        self.play(Create(axes_422), Write(x_label_422), Write(y_label_422))
        pixel_values_422 = create_ycbcr_grid(self, axes_422, horizontal_subsample=True)
        self.wait(3)  # Show 422 for 3 seconds

        # Remove 4:2:2 completely
        self.play(
            *[
                FadeOut(mob)
                for mob in [
                    format_422_label,
                    axes_422,
                    x_label_422,
                    y_label_422,
                    pixel_values_422,
                ]
            ]
        )
        self.wait(1)  # Clear pause between formats

        # Show 4:2:0
        format_420_label = Text("4:2:0 - Quarter Color Resolution", font_size=36)
        format_420_label.to_edge(UP)
        self.play(Write(format_420_label))

        axes_420 = Axes(
            x_range=[0, 5, 1],
            y_range=[0, 3, 1],
            x_length=8,
            y_length=4,
            axis_config={"color": WHITE},
        )

        x_label_420 = Text("1920", font_size=24)
        y_label_420 = Text("1080", font_size=24)
        x_label_420.next_to(axes_420.x_axis.get_end(), DOWN)
        y_label_420.next_to(axes_420.y_axis.get_end(), LEFT)

        self.play(Create(axes_420), Write(x_label_420), Write(y_label_420))
        pixel_values_420 = create_ycbcr_grid(
            self, axes_420, horizontal_subsample=True, vertical_subsample=True
        )
        self.wait(3)  # Show 420 for 3 seconds

        # Add final explanation
        final_explanation = Text(
            "4:2:0 is most common - used in H.264, H.265, and streaming video",
            font_size=24,
        )
        final_explanation.to_edge(DOWN)
        self.play(Write(final_explanation))
        self.wait(2)

        # Clear everything before showing difference image
        self.play(
            *[
                FadeOut(mob)
                for mob in [
                    format_420_label,
                    axes_420,
                    x_label_420,
                    y_label_420,
                    pixel_values_420,
                    final_explanation,
                ]
            ]
        )
        self.wait(1)

        # Show subsampling difference image
        diff_title = Text("Subsampling Difference Visualization (×10)", font_size=36)
        diff_title.to_edge(UP)
        self.play(Write(diff_title))

        diff_image = ImageMobject("imgs/subsampling-diff.png")
        # Set height to match previous image size while maintaining aspect ratio
        diff_image.set_width(14)  # Set to frame width with margin
        diff_image.move_to(ORIGIN)

        self.play(FadeIn(diff_image))
        self.wait(3)
