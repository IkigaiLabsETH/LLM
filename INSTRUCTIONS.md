https://replicate.com/docs/guides/push-a-model

Here are concise instructions for pushing a model to Replicate, based on the guide at [https://replicate.com/docs/guides/push-a-model](https://replicate.com/docs/guides/push-a-model):

1. Prerequisites:
   - Trained model in a directory on your computer
   - Docker installed and running
   - GPU machine with NVIDIA Container Toolkit (if GPU needed)
   - Replicate account

2. Create a model page on [replicate.com/create](https://replicate.com/create)

3. Install Cog:
   ```bash
   sudo curl -o /usr/local/bin/cog -L https://github.com/replicate/cog/releases/latest/download/cog_`uname -s`_`uname -m`
   sudo chmod +x /usr/local/bin/cog
   ```

4. Initialize Cog in your model directory:
   ```bash
   cd path/to/your/model
   cog init
   ```

5. Define dependencies in `cog.yaml`:
   - Specify Python version, packages, and GPU requirements

6. Update `predict.py`:
   - Implement `setup()` and `predict()` methods
   - Define input types and descriptions

7. Add `predict: "predict.py:Predictor"` to `cog.yaml`

8. Test locally:
   ```bash
   cog predict -i input1=value1 -i input2=value2
   ```

9. Push to Replicate:
   ```bash
   cog login
   cog push r8.im/<your-username>/<your-model-name>
   ```

10. Run predictions using the Replicate Python client or HTTP API

Remember to refer to the full documentation for detailed information on each step.