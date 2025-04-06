from manim import *
import random

config.frame_width = 16
config.frame_height = 9


class BinaryToColor(Scene):
    def construct(self):
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

        # Part 2: How these represent colors
        title2 = Text("How do these 0s and 1s represent colors?", font_size=36)
        self.play(FadeOut(binary_cluster), Write(title2))
        self.wait(1)
        self.play(FadeOut(title2))

        # Part 3: 8 bits for color values
        title3 = Text("8 bits = 1 color value", font_size=36)
        self.play(Write(title3))
        self.wait(1)
        self.play(FadeOut(title3))

        # Create 8 bit boxes with random initial values
        bits = []
        bit_boxes = []
        initial_values = [random.choice(["0", "1"]) for _ in range(8)]
        for i in range(8):
            box = Square(side_length=0.8)
            box.set_fill(WHITE, opacity=0.2)
            box.set_stroke(WHITE, width=2)
            box.shift(LEFT * (3.5 - i))
            bit = Text(initial_values[i], font_size=36)
            bit.move_to(box.get_center())
            bits.append(bit)
            bit_boxes.append(box)
            self.play(Create(box), Write(bit))

        # Part 4: Show all possible combinations
        title4 = Text("How many possible combinations?", font_size=36)
        title4.to_edge(UP)
        self.play(Write(title4))

        # Show multiplication of 2s
        twos = VGroup()
        for i in range(8):
            two = Text("2", font_size=36)
            two.next_to(bit_boxes[i], UP)
            if i < 7:
                times = Text("×", font_size=36)
                times.next_to(two, RIGHT)
                twos.add(two, times)
            else:
                twos.add(two)

        self.play(Write(twos))
        self.wait(1)

        # Show equals 256
        equals = Text("= 256", font_size=36)
        equals.next_to(twos, RIGHT)
        self.play(Write(equals))
        self.wait(1)

        # Part 5: Show RGB squares with values
        self.play(
            FadeOut(twos),
            FadeOut(equals),
            FadeOut(title4),
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


class RGBPixelGrid(Scene):
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

        for i in range(4):
            for j in range(3):
                # Create RGB values
                r = random.randint(0, 255)
                g = random.randint(0, 255)
                b = random.randint(0, 255)

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
            "Each pixel contains 3 color values (R,G,B)\nEach value ranges from 0 to 255",
            font_size=24,
        )
        explanation.to_edge(DOWN)
        self.play(Write(explanation))
        self.wait(2)


class BitDepthExplanation(Scene):
    def construct(self):
        # Create title
        title = Text("8-bit Color Depth", font_size=48)
        self.play(Write(title))
        self.wait(1)
        self.play(FadeOut(title))

        # Create 8 binary digits
        bits = []
        bit_boxes = []
        bit_values = []
        bit_positions = []

        # Create bit boxes and labels
        for i in range(8):
            # Create box for each bit
            box = Square(side_length=0.8)
            box.set_fill(WHITE, opacity=0.2)
            box.set_stroke(WHITE, width=2)

            # Position boxes from right to left
            box.shift(LEFT * (3.5 - i))

            # Create bit label (0 or 1)
            bit = Text("0", font_size=36)
            bit.move_to(box.get_center())

            # Create position value (2^i)
            value = Text(f"2^{i}", font_size=24)
            value.next_to(box, UP)

            bits.append(bit)
            bit_boxes.append(box)
            bit_values.append(value)
            bit_positions.append(i)

            self.play(Create(box), Write(value))

        # Animate bits turning on one by one
        decimal_value = 0
        for i in range(8):
            # Update bit to 1
            new_bit = Text("1", font_size=36)
            new_bit.move_to(bit_boxes[i].get_center())

            # Calculate new decimal value
            decimal_value += 2**i

            # Create decimal value display
            decimal_text = Text(f"= {decimal_value}", font_size=36)
            decimal_text.next_to(bit_boxes[-1], RIGHT)

            self.play(Transform(bits[i], new_bit), Write(decimal_text))
            self.wait(0.5)

            if i < 7:  # Don't remove the last decimal text
                self.play(FadeOut(decimal_text))

        # Final explanation
        explanation = Text(
            "8 bits = 2⁸ = 256 possible values (0-255)\nper color channel", font_size=36
        )
        explanation.to_edge(DOWN)
        self.play(Write(explanation))
        self.wait(2)


class DefaultTemplate(Scene):
    def construct(self):
        circleRed = Circle()  # create a circle
        circleRed.set_fill("#FF0000", opacity=1)  # pure red
        circleRed.shift(LEFT * 2.5)  # move left
        circleRed.set_stroke(width=0)  # set the stroke width

        circleGreen = Circle()  # create a circle
        circleGreen.set_fill("#00FF00", opacity=1)  # pure green
        circleGreen.set_stroke(width=0)  # set the stroke width
        # green circle stays in center

        circleBlue = Circle()  # create a circle
        circleBlue.set_fill("#0000FF", opacity=1)  # pure blue
        circleBlue.set_stroke(width=0)  # set the stroke width
        circleBlue.shift(RIGHT * 2.5)  # move right

        self.play(
            Create(circleRed), Create(circleGreen), Create(circleBlue)
        )  # show the shapes on screen


class ValueRangeComparison(Scene):
    def construct(self):
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
        eight_bit_label = Text("6.22 MB", font_size=20)
        eight_bit_label.move_to(eight_bit_storage)

        ten_bit_storage = Rectangle(
            width=2.5, height=1, color=GREEN
        )  # Smaller rectangles
        ten_bit_storage.set_fill(GREEN, opacity=0.3)
        ten_bit_storage.next_to(eight_bit_storage, RIGHT, buff=0.6)
        ten_bit_label = Text("7.78 MB", font_size=20)
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


class StorageCalculation(Scene):
    def construct(self):
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


class TenBitComparison(Scene):
    def construct(self):
        # Start with 8-bit display
        title1 = Text("8-bit Color Depth", font_size=36)
        title1.to_edge(UP)  # Move title to top
        self.play(Write(title1))
        self.wait(1)
        self.play(FadeOut(title1))

        # Create 8 bit boxes with random initial values
        bits_8 = []
        bit_boxes_8 = []
        initial_values = [random.choice(["0", "1"]) for _ in range(8)]
        for i in range(8):
            box = Square(side_length=0.8)
            box.set_fill(WHITE, opacity=0.2)
            box.set_stroke(WHITE, width=2)
            box.shift(LEFT * (3.5 - i))
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
            box.set_fill(WHITE, opacity=0.2)
            box.set_stroke(WHITE, width=2)
            box.shift(LEFT * (3.5 - i))
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

        # Memory comparison
        self.play(
            FadeOut(VGroup(*bits_10)),
            FadeOut(VGroup(*bit_boxes_10)),
            FadeOut(twos_10),
            FadeOut(equals_10),
        )

        # HD resolution info
        hd_text = Text("HD Resolution: 1920 × 1080 pixels", font_size=36)
        hd_text.to_edge(UP)
        self.play(Write(hd_text))

        # Memory calculation
        eight_bit_calc = Text(
            "8-bit: 1920 × 1080 × 3 channels × 8 bits = 49,766,400 bits\n" "= 6.22 MB",
            font_size=32,
        )
        eight_bit_calc.next_to(hd_text, DOWN, buff=1)

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

        # Percentage increase
        increase_text = Text(
            "25% increase in file size\n" "4× more color values per channel",
            font_size=36,
        )
        increase_text.to_edge(DOWN)
        self.play(Write(increase_text))
        self.wait(2)


class BitDepthComparison(Scene):
    def construct(self):
        # Title
        title = Text("8-bit vs 10-bit Storage Comparison", font_size=32)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # 8-bit calculation
        eight_bit_calc = Text(
            "1920 × 1080 × 3 (RGB) × 8 (bits) = 49,766,400 bits", font_size=28
        )
        eight_bit_calc.shift(UP * 2)
        self.play(Write(eight_bit_calc))
        self.wait(1)

        # 8-bit bytes
        eight_bit_bytes = Text("49,766,400 ÷ 8 = 6,220,800 bytes", font_size=28)
        eight_bit_bytes.next_to(eight_bit_calc, DOWN, buff=0.5)
        eight_bit_bytes.align_to(eight_bit_calc, LEFT)
        self.play(Write(eight_bit_bytes))
        self.wait(1)

        # 8-bit MB result
        eight_bit_mb = Text("= 6.22 MB", font_size=28, color=BLUE)
        eight_bit_mb.next_to(eight_bit_bytes, DOWN, buff=0.5)
        eight_bit_mb.align_to(eight_bit_calc, LEFT)
        self.play(Write(eight_bit_mb))
        self.wait(1)

        # 10-bit calculation
        ten_bit_calc = Text(
            "1920 × 1080 × 3 (RGB) × 10 (bits) = 62,208,000 bits", font_size=28
        )
        ten_bit_calc.next_to(eight_bit_mb, DOWN, buff=1)
        ten_bit_calc.align_to(eight_bit_calc, LEFT)
        self.play(Write(ten_bit_calc))
        self.wait(1)

        # 10-bit bytes
        ten_bit_bytes = Text("62,208,000 ÷ 8 = 7,776,000 bytes", font_size=28)
        ten_bit_bytes.next_to(ten_bit_calc, DOWN, buff=0.5)
        ten_bit_bytes.align_to(eight_bit_calc, LEFT)
        self.play(Write(ten_bit_bytes))
        self.wait(1)

        # 10-bit MB result
        ten_bit_mb = Text("= 7.78 MB", font_size=28, color=GREEN)
        ten_bit_mb.next_to(ten_bit_bytes, DOWN, buff=0.5)
        ten_bit_mb.align_to(eight_bit_calc, LEFT)
        self.play(Write(ten_bit_mb))
        self.wait(1)


class BitDepthGrowth(Scene):
    def construct(self):
        # Title
        title = Text("8-bit vs 10-bit: Value Growth vs Storage Growth", font_size=32)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # 8-bit calculation
        eight_bit_calc = Text(
            "8-bit: 2 × 2 × 2 × 2 × 2 × 2 × 2 × 2 = 256", font_size=28
        )
        eight_bit_calc.shift(UP * 2)
        self.play(Write(eight_bit_calc))
        self.wait(1)

        # 10-bit calculation
        ten_bit_calc = Text(
            "10-bit: 2 × 2 × 2 × 2 × 2 × 2 × 2 × 2 × 2 × 2 = 1024", font_size=28
        )
        ten_bit_calc.next_to(eight_bit_calc, DOWN, buff=0.8)
        ten_bit_calc.align_to(eight_bit_calc, LEFT)
        self.play(Write(ten_bit_calc))
        self.wait(1)

        # Value growth explanation
        value_growth = Text(
            "4× more color values (256 → 1024)", font_size=28, color=GREEN
        )
        value_growth.next_to(ten_bit_calc, DOWN, buff=0.8)
        value_growth.align_to(eight_bit_calc, LEFT)
        self.play(Write(value_growth))
        self.wait(1)

        # Create 8-bit binary display
        eight_bit_binary = VGroup()
        for i in range(8):
            bit = Text("0", font_size=36)
            bit.move_to([i - 3.5, -1, 0])
            eight_bit_binary.add(bit)

        eight_bit_label = Text("8 bits", font_size=28)
        eight_bit_label.next_to(eight_bit_binary, DOWN, buff=0.5)
        self.play(Write(eight_bit_binary), Write(eight_bit_label))
        self.wait(1)

        # Create 10-bit binary display
        ten_bit_binary = VGroup()
        for i in range(10):
            bit = Text("0", font_size=36)
            bit.move_to([i - 4.5, -2.5, 0])
            ten_bit_binary.add(bit)

        ten_bit_label = Text("10 bits", font_size=28)
        ten_bit_label.next_to(ten_bit_binary, DOWN, buff=0.5)
        self.play(Write(ten_bit_binary), Write(ten_bit_label))
        self.wait(1)

        # Storage ratio
        storage_ratio = Text("10/8 = 1.25 (25% more storage)", font_size=28, color=BLUE)
        storage_ratio.next_to(ten_bit_label, DOWN, buff=0.8)
        self.play(Write(storage_ratio))
        self.wait(1)

        # Final comparison
        final_comparison = Text(
            "4× more precision for 25% more storage", font_size=32, color=YELLOW
        )
        final_comparison.next_to(storage_ratio, DOWN, buff=1)
        self.play(Write(final_comparison))
        self.wait(2)
